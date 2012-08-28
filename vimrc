"===============================================================
" GENERAL
"
colorscheme darkblue

set nocompatible               " be iMproved
set directory=$HOME/.vim/tmp   " put swapfiles away

set wildmode=longest,list
set scrolloff=3
set textwidth=0

set number                      " display line number
nnoremap <F2> :set nonumber!<CR>

set mouse=a                     " enable mouse scrolling

set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue 



"==============================================================
" INDENTATION
"
set tabstop=2
set softtabstop=2
set shiftwidth=2
set smarttab
set expandtab



"==============================================================
" NAVIGATION
"
map ê <C-D>
map ë <C-U>
map <M-j> <C-D>
map <M-k> <C-U>

map ì $
map è ^ 

noremap  <Up> ""
noremap! <Up> <Esc>
noremap  <Down> ""
noremap! <Down> <Esc>
noremap  <Left> ""
noremap! <Left> <Esc>
noremap  <Right> ""
noremap! <Right> <Esc> 


"==============================================================
" COMMENTS
"map :s/^/\#:s/^\#\#/
map ,# :call CommentLineToEnd('#')<CR>+
map ,, :call CommentLineToEnd('#')<CR>+



"==============================================================
" SEARCH
"
set incsearch
set ignorecase
set smartcase



"===============================================================
" AUTOCOMMANDS
"
autocmd BufWrite        *.py,*.sh  !chmod +x %



"===============================================================
" BUFFERS
"
set hidden

nnoremap <C-L> :bnext<CR>
nnoremap <C-H> :bprev<CR>
"
"nnoremap <M-`> :b#<CR>
"nnoremap <M-space> :bnext<CR>
"nnoremap <M-1> :1b<CR>
"nnoremap <M-2> :2b<CR>
"nnoremap <M-3> :3b<CR>
"nnoremap <M-4> :4b<CR>
"nnoremap <M-5> :5b<CR>
"nnoremap <M-6> :6b<CR>
"nnoremap <M-7> :7b<CR>
"nnoremap <M-8> :8b<CR>
"nnoremap <M-9> :9b<CR>
"nnoremap <M-0> :10b<CR>
"
"":MiniBufExplorer
"":CMiniBufExplorer
"":UMiniBufExplorer
"nnoremap <F3> :TMiniBufExplorer<CR>
"
"let g:miniBufExplSplitBelow=0
"let g:miniBufExplVSplit = 20
"let g:miniBufExplorerMoreThanOne=0
"
""enable the optional mapping of Control + Vim Direction Keys
""[hjkl] to window movement commands
""let g:miniBufExplMapWindowNavVim = 1
"
""enable the optional mapping of <C-TAB> and <C-S-TAB> to mappings
""that will move to the next and previous (respectively) window
""let g:miniBufExplMapCTabSwitchWindows = 1

