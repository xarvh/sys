
python << endpy

import sys
import os
sys.path.insert(0, "%s/.vim/" % os.getenv('HOME'))
from vimrc import *

endpy



"===============================================================
" GENERAL
"
let mapleader = ' '
set nocompatible               " be iMproved
set directory=$HOME/.vim/tmp   " put swapfiles away

set clipboard=unnamedplus      " copy to clipboard
set mouse=a                    " enable mouse scrolling
set shortmess=atI

set wildmode=longest,list
set scrolloff=3
set textwidth=0

nnoremap <leader><leader> :
nnoremap <F9> :source $MYVIMRC<CR>
filetype plugin on
filetype indent on


"===============================================================
" APPEARANCE
"
colorscheme darkblue
set guioptions=acegi
set gfn=Monospace\ Bold\ 11
set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue

nnoremap <leader>n :set nonumber!<CR>  " toggle line number
nnoremap <leader>w :set wrap!<CR>

highlight TrailingWhitespace ctermbg=red guibg=red
match TrailingWhitespace /\s\+$/

"===============================================================
" EDITING
"
inoremap <Tab> <C-N>
vnoremap . :normal .<CR>
nnoremap <leader>5 me%mw%r `wx`e
nnoremap Y y$


"==============================================================
" INDENTATION
"
set tabstop=2
set softtabstop=2
set shiftwidth=2
set smarttab
set expandtab


"==============================================================
" LANGUAGE SPECIFICS
"
" Beautify JSON
nnoremap <leader>b :%!python -mjson.tool<CR>

" Compile Coffee
vmap <leader>c <esc>:'<,'>:CoffeeCompile<CR>
map <leader>c :CoffeeCompile<CR>
command -nargs=1 C CoffeeCompile | :<args>


"==============================================================
" NAVIGATION
"
set whichwrap+=h,l,<,>,[,]

map <C-k> <C-U>
map <C-j> <C-D>
map L $
map H ^


"==============================================================
" EXALTED DOTS

map <F5> :python removeExaltedDot()<CR>
map <F6> :python addExaltedDot()<CR>


"==============================================================
" COMMENTS

function! MultiComment(after_spaces)
      if 0
  elseif &filetype == 'jade' | let c = '\/\/'
  elseif &filetype == 'vim' | let c = '"'
  else | let c = '#'
  endif

  let s = a:after_spaces ? "\\(\\s*\\)" : ""

  execute "s/^".s."/\\1".c."/"
  execute "s/^".s.c.c."/\\1/e"
endfunction

map <silent> - :call MultiComment(0)<CR>+


"==============================================================
" SEARCH (& REPLACE)
"
nnoremap <leader>r :%s/
vnoremap <leader>r "hy:%s/<C-r>h/
set incsearch
set ignorecase
set smartcase

map <leader>f :AckFile!<space>
map <leader>a :Ack!<space>
map <leader>8 :Ack! <cword><CR>


"===============================================================
" BUFFERS and WINDOWS
"
set hidden

nnoremap ' <C-w>w
nnoremap <leader>n :tabnew<CR>

nnoremap <C-L> :bnext<CR>
nnoremap <C-H> :bprev<CR>

