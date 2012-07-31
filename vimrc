"===============================================================
" GENERAL
"
set nocompatible               " be iMproved
set wildmode=longest,list
set scrolloff=3
set textwidth=0
set number                      " display line number

set cursorline
hi CursorLine cterm=NONE ctermbg=darkblue ctermfg=white guibg=darkred guifg=white



"==============================================================
" INDENTATION
"
set tabstop=2
set softtabstop=2
set shiftwidth=2
set smarttab
set expandtab



"==============================================================
" SEARCH
"
set incsearch
set ignorecase
set smartcase



"===============================================================
" AUTOCOMMANDS
"
autocmd BufWrite        *.rb,*.py,*.sh  !chmod +x %



"===============================================================
" BUFFERS
"
set hidden

nnoremap <M-`> :b#<CR>
nnoremap <M-space> :bnext<CR>
nnoremap <M-1> :1b<CR>
nnoremap <M-2> :2b<CR>
nnoremap <M-3> :3b<CR>
nnoremap <M-4> :4b<CR>
nnoremap <M-5> :5b<CR>
nnoremap <M-6> :6b<CR>
nnoremap <M-7> :7b<CR>
nnoremap <M-8> :8b<CR>
nnoremap <M-9> :9b<CR>
nnoremap <M-0> :10b<CR>

":MiniBufExplorer
":CMiniBufExplorer
":UMiniBufExplorer
nnoremap <M-m> :TMiniBufExplorer<CR>

let g:miniBufExplSplitBelow=0
let g:miniBufExplVSplit = 20
let g:miniBufExplorerMoreThanOne=0

"enable the optional mapping of Control + Vim Direction Keys
"[hjkl] to window movement commands
"let g:miniBufExplMapWindowNavVim = 1

"enable the optional mapping of <C-TAB> and <C-S-TAB> to mappings
"that will move to the next and previous (respectively) window
"let g:miniBufExplMapCTabSwitchWindows = 1

