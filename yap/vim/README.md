# Yap Vim Plugin (Experimental)

Visualize real-time voice-to-text transcripts directly inside Vim/Neovim.

## Requirements

*   Neovim (0.5+) with `jobstart` support.
*   Python 3.
*   `websockets` python library installed.
*   `uv` (optional, but recommended if running from source).

## Installation

### 1. Manual
Copy the `yap/vim` directory to your Vim runtime path (e.g., `~/.config/nvim/pack/plugins/start/yap`).

### 2. Plugin Manager (e.g., vim-plug)
Add to your `init.vim` or `.vimrc`:
```vim
Plug 'dannyrosen/yap', {'rtp': 'yap/vim'}
```
(Adjust path if the repo structure differs).

## Usage

1.  **Start the Yap Server**:
    Ensure `yap-server` is running (locally or remotely via SSH tunnel).
    ```bash
    uv run yap-server
    ```

2.  **In Vim**:
    Run the command:
    ```vim
    :YapStart
    ```
    This will open a scratch buffer and start displaying the transcript in real-time.

3.  **Stop**:
    ```vim
    :YapStop
    ```

## Configuration

Set these variables in your `init.vim` if needed:

```vim
let g:yap_server_host = "localhost"
let g:yap_server_port = 9090
" If you want to use a specific python interpreter instead of 'uv run python':
let g:yap_python_cmd = "/path/to/venv/bin/python" 
```
