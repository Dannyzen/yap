" Yap Vim Plugin - Voice to Text Integration
" Language: Vim Script
" Maintainer: Danny Rosen

if exists("g:loaded_yap")
    finish
endif
let g:loaded_yap = 1

let s:yap_job = v:null
let s:yap_buf = -1
let s:script_path = expand('<sfile>:p:h:h') . '/python/yap_monitor.py'

" Configuration
if !exists("g:yap_server_host")
    let g:yap_server_host = "localhost"
endif
if !exists("g:yap_server_port")
    let g:yap_server_port = 9090
endif
if !exists("g:yap_auto_scroll")
    let g:yap_auto_scroll = 1
endif

function! s:ensure_buffer()
    if s:yap_buf == -1 || !bufexists(s:yap_buf)
        " Create a new scratched buffer
        let l:name = 'YapTranscript'
        if bufexists(l:name)
            " If it already exists (but s:yap_buf lost track), re-use it
            let s:yap_buf = bufnr(l:name)
        else
            execute 'vsplit ' . l:name
            let s:yap_buf = bufnr('%')
            setlocal buftype=nofile
            setlocal bufhidden=hide
            setlocal noswapfile
            setlocal nobuflisted
            setlocal filetype=txt
            setlocal wrap
            " Add some header
            call append(0, "== Yap Transcript Started ==")
            call append(1, "")
        endif
    endif
    return s:yap_buf
endfunction

function! s:on_stdout(job_id, data, event)
    let l:buf = s:ensure_buffer()
    
    " Neovim passes data as a list of strings
    if type(a:data) == v:t_list
        let l:lines = a:data
    else
        let l:lines = [a:data]
    endif

    " Filter out empty lines often sent by job control
    let l:lines = filter(l:lines, 'v:val != ""')

    if empty(l:lines)
        return
    endif

    " Append lines to buffer
    call nvim_buf_set_lines(l:buf, -1, -1, v:false, l:lines)

    " Auto-scroll if enabled
    if g:yap_auto_scroll
        let l:win_id = bufwinid(l:buf)
        if l:win_id != -1
            call nvim_win_set_cursor(l:win_id, [line('$', l:win_id), 0])
        endif
    endif
endfunction

function! s:on_refresh(job_id, data, event)
    " Vim8 handling if needed, but targeting Neovim mostly for async jobs
endfunction

function! YapStart()
    if s:yap_job != v:null
        echo "Yap monitor is already running."
        return
    endif

    echo "Starting Yap monitor..."
    call s:ensure_buffer()

    " Default to system python3. User can override with g:yap_python_cmd.
    let l:cmd = ['python3', s:script_path, '--host', g:yap_server_host, '--port', string(g:yap_server_port)]
    
    " If user defined a custom command (e.g. 'uv run python' or '/path/to/venv/bin/python')
    if exists("g:yap_python_cmd")
        " If it's a string, split it (e.g. "uv run python")
        if type(g:yap_python_cmd) == v:t_string
             let l:cmd = split(g:yap_python_cmd) + [s:script_path, '--host', g:yap_server_host, '--port', string(g:yap_server_port)]
        else
             " Assume list
             let l:cmd = g:yap_python_cmd + [s:script_path, '--host', g:yap_server_host, '--port', string(g:yap_server_port)]
        endif
    endif

    " Check for Neovim vs Vim8 async support
    if exists('*jobstart')
        " Neovim
        let s:opts = {
            \ 'on_stdout': function('s:on_stdout'),
            \ 'on_stderr': function('s:on_stdout'), 
            \ 'detach': 1
        \ }
        let s:yap_job = jobstart(l:cmd, s:opts)
        
        if s:yap_job <= 0
            echoerr "Failed to start Yap monitor job."
            let s:yap_job = v:null
        else
            echo "Yap connected (Neovim)."
        endif
        
    elseif exists('*job_start')
        " Vim 8+
        " Vim jobs use callbacks with (channel, msg)
        let s:opts = {
            \ 'out_cb': function('s:on_stdout_vim'),
            \ 'err_cb': function('s:on_stdout_vim'),
            \ 'exit_cb': function('s:on_exit_vim'),
            \ 'mode': 'nl'
        \ }
        let s:yap_job = job_start(l:cmd, s:opts)
        
        if job_status(s:yap_job) != 'run'
            echoerr "Failed to start Yap monitor job."
            let s:yap_job = v:null
        else
            echo "Yap connected (Vim)."
        endif
        
    else
        echoerr "Your Vim version does not support async jobs (needs +job)."
    endif
endfunction

function! s:on_stdout_vim(channel, msg)
    " Vim8 callback signature is different: (channel, msg_string)
    " It often calls this per line if mode is 'nl'
    let l:buf = s:ensure_buffer()
    
    if a:msg == ""
        return
    endif
    
    " Append single line
    call appendbufline(l:buf, '$', a:msg)

    " Auto-scroll
    if g:yap_auto_scroll
        let l:win_id = bufwinid(l:buf)
        if l:win_id != -1
            python3 import vim
            " Use python to scroll safely in older vim or just straightforward command
            " call win_execute(l:win_id, "normal! G") (Vim 8.1.1418+)
            if exists('*win_execute')
                call win_execute(l:win_id, "normal! G")
            endif
        endif
    endif        
endfunction

function! s:on_exit_vim(job, status)
    let s:yap_job = v:null
    echo "Yap monitor exited."
endfunction

function! YapStop()
    if s:yap_job != v:null
        if exists('*jobstop')
            " Neovim
            call jobstop(s:yap_job)
        elseif exists('*job_stop')
            " Vim 8
            call job_stop(s:yap_job)
        endif
        let s:yap_job = v:null
        echo "Yap monitor stopped."
    endif
endfunction

function! YapToggle()
    if s:yap_job != v:null
        call YapStop()
    else
        call YapStart()
    endif
endfunction

command! YapStart call YapStart()
command! YapStop call YapStop()
command! YapToggle call YapToggle()
command! YapLog execute 'sbuffer ' . s:ensure_buffer()
