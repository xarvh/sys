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

nnoremap <F9> :source $MYVIMRC<cr>
filetype plugin on
filetype indent on

" Block mouse middle click
map <MiddleMouse> <Nop>
imap <MiddleMouse> <Nop>
map <2-MiddleMouse> <Nop>
imap <2-MiddleMouse> <Nop>
map <3-MiddleMouse> <Nop>
imap <3-MiddleMouse> <Nop>
map <4-MiddleMouse> <Nop>
imap <4-MiddleMouse> <Nop>

"===============================================================
" APPEARANCE
"
colorscheme darkblue
set guioptions=acegi
set gfn=Monospace\ Bold\ 11
set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue 

nnoremap <leader>l :set nonumber!<CR>  " toggle line number
nnoremap <leader>w :set wrap!<CR>


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

"map ê <C-D>
"map ë <C-U>
"map <M-j> <C-D>
"map <M-k> <C-U>

map L $
map H ^

noremap  <Up> ""
noremap  <Down> ""
noremap  <Left> ""
noremap! <Left> <Esc>
noremap  <Right> ""
noremap! <Right> <Esc>


"==============================================================
" EXALTED DOTS
function! AddDot()

"  while getline(".")[col(".")-1] == '1'
"    normal l
"  endwhile

  execute "/\\s"
"  while getline(".")[col(".")-2] == '0'
"    normal h
"  endwhile

"  let c = getline(".")[col(".")-1]
"
"  if c == '0'
"
"    normal yyp
"  normal dawPbyl
"  echo getline(".")[col(".")-1] 
"  if getline(".")[col(".")-1] == '0'
"    normal r1
"  elseif @ == '1'
"    echo 'hello'
"  else
"    normal rx
"  endif

"echo @

endfunction

map <F6> :call AddDot()<cr>

"map <F5> /$\\|[ ○]<cr>:s?●?○<cr>
"map <F6> ?^\\|[ ●]<cr>:s/○/●<cr>
"map <F5> /$\|[0 ]/<cr>:s?1/0<cr>
"map <F6> ?^\\|[ 1]<cr><cr>:s/0/1<cr>


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
" SEARCH
"
nnoremap <leader>r :%s/
set incsearch
set ignorecase
set smartcase

map <leader>f :AckFile!<space>
map <leader>a :Ack!<space>
map <leader>8 :Ack! <cword><cr>


"===============================================================
" BUFFERS and WINDOWS
"
set hidden

nnoremap ' <C-w>w
nnoremap <leader>n :tabnew<cr>

nnoremap <C-L> :bnext<CR>
nnoremap <C-H> :bprev<CR>

