"===============================================================
" GENERAL
"
set nocompatible               " be iMproved
set directory=$HOME/.vim/tmp   " put swapfiles away

set clipboard=unnamedplus       " copy to clipboard

set wildmode=longest,list
set scrolloff=3
set textwidth=0


"===============================================================
" APPEARANCE
"
colorscheme darkblue
set guioptions=acegi
set gfn=Monospace\ Bold\ 11
set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue 

nnoremap <F2> :set nonumber!<CR>  " toggle line number


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
set mouse=a                    " enable mouse scrolling

map ê <C-D>
map ë <C-U>
map <M-j> <C-D>
map <M-k> <C-U>

map ì $
map è ^ 

"noremap  <Up> ""
"noremap! <Up> <Esc>
"noremap  <Down> ""
"noremap! <Down> <Esc>
"noremap  <Left> ""
"noremap! <Left> <Esc>
"noremap  <Right> ""
"noremap! <Right> <Esc> 


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

map <silent> , :call MultiComment(0)<CR>+
map <silent> ; :call MultiComment(1)<CR>+


"==============================================================
" SEARCH
"
nnoremap <F4> :%s/
set incsearch
set ignorecase
set smartcase



"===============================================================
" AUTOCOMMANDS
"
"autocmd BufWrite        *.py,*.sh  !chmod +x %


"===============================================================
" BUFFERS
"
set hidden

nnoremap <C-L> :bnext<CR>
nnoremap <C-H> :bprev<CR>
