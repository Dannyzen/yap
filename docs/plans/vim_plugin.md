# Vim Plugin Implementation Plan (`vim-yap`)

This document outlines the experimental implementation plan for a Vim plugin that integrates with the Yap voice-to-text server.

## Objective
Enable Vim/Neovim users to visualize real-time transcriptions and dictate text directly into buffers using the Yap ecosystem.

## Architecture

### 1. Connection Strategy
The plugin will act as a **Monitor Client** rather than an Audio Source. 
*   **Reasoning**: Vim is text-centric. Audio capture should be handled by the external `yap` client (daemon) running in the background. Vim simply subscribes to the text stream.
*   **Protocol**: WebSocket connection to `ws://localhost:9090` (default).

### 2. Implementation Logic (Python 3 Interface)
Since `yap` already has a robust Python client library, we will leverage Vim's `if_python3` feature.

**Core Components**:
1.  **`plugin/yap.vim`**: VimScript wrapper for commands and keybindings.
2.  **`python/yap_vim_adapter.py`**: Python script running inside Vim process to handle async WebSocket communication.

### 3. Features

#### A. Live Transcript Buffer (`:YapLog`)
*   Opens a split window (scratch buffer).
*   Appends incoming transcription segments in real-time.
*   Auto-scrolls to the bottom.
*   Useful for: Meeting notes, monitoring dictation without cursor interference.

#### B. Direct Dictation (`:YapStart`)
*   Inserts text at the current cursor position in the active buffer.
*   Handles "final" vs "partial" updates (overwriting partial text until finalized).

#### C. Status Indicator
*   Shows connection status in the statusline (e.g., `[Yap: Connected]`).

## Technical Challenges & Solutions

### 1. Blocking UI
**Challenge**: Python's `asyncio` loop blocks Vim's main thread.
**Solution**: 
*   **Neovim**: Use `uv` loop integration or remote plugin architecture.
*   **Vim 8+**: Use `job_start` / `channel` for non-blocking I/O, or run the Python client in a separate thread/process that communicates back via `vim.async_call` (if available) or polling.
*   **Universal**: Run a separate `yap-vim-bridge` process. The plugin reads from its stdout via Vim's `job` control.

### 2. Partial vs Final Text
**Challenge**: Whisper updates partial text rapidly.
**Solution**: 
*   Store the *last partial segment length*.
*   On update: Delete last N characters -> Insert new partial.
*   On finalize: Commit text -> Reset partial counter.

## Roadmap

### Phase 1: Prototype (The "Monitor")
1.  Simple Python script to connect to `ws://localhost:9090`.
2.  Print to a dedicated Vim buffer using `vim.command()`.
3.  Prove non-blocking async execution.

### Phase 2: Integration
1.  Implement `:YapConnect` and `:YapDisconnect`.
2.  Create `doc/yap.txt` help file.

### Phase 3: Advanced
1.  Key mappings for toggle recording (`<leader>yr`).
2.  Statusline integration.

## Files Structure
```
yap/
├── plugin/
│   └── yap.vim         # Command definitions
├── python/
│   └── yap_client.py   # WebSocket logic
└── doc/
    └── yap.txt         # Help documentation
```
