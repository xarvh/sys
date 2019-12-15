
"===============================================================
" GENERAL
"

call plug#begin('~/.vim/plugged')

Plug 'calviken/vim-gdscript3'
Plug 'justinmk/vim-dirvish'
Plug 'jeetsukumaran/vim-buffergator'
Plug 'tpope/vim-fugitive'
Plug 'mileszs/ack.vim'
Plug 'elmcast/elm-vim'

"Plug 'tpope/vim-vinegar'

call plug#end()

"let g:deoplete#omni_patterns.elm = '\.'
let g:elm_detailed_complete = 1
let g:elm_format_autosave = 0


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

" https://github.com/webpack/webpack/issues/781#issuecomment-95523711
set backupcopy=yes

nnoremap <CR> :
nnoremap <F9> :source $MYVIMRC<CR>
filetype plugin on
filetype indent on



"===============================================================
" FILE & BUFFER BROWSING
"
"


let g:buffergator_suppress_keymaps = 1
let g:buffergator_autoexpand_on_split = 0
nnoremap <Tab> :BuffergatorToggle<CR>

let dirvish_mode = ':sort ,^.*/,'

"nnoremap - :Explore<CR>
"let g:netrw_banner = 0
"https://github.com/tpope/vim-vinegar/issues/13#issuecomment-47133890


"===============================================================
" APPEARANCE
"
colorscheme darkblue
set guioptions=acegi
set gfn=Monospace\ Bold\ 11
set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue

nnoremap <leader>w :set wrap!<CR>

highlight TrailingWhitespace ctermbg=red guibg=red
match TrailingWhitespace /\s\+$/


"===============================================================
" EDITING
"
function! Tab_Or_Complete()
  if col('.')>1 && strpart( getline('.'), col('.')-2, 3 ) =~ '^\w'
    return "\<C-n>"
    "return "\<C-x>\<C-o>"
  else
    return "\<Tab>"
  endif
endfunction

inoremap <Tab> <C-R>=Tab_Or_Complete()<CR>
set dictionary="/usr/dict/words"

vnoremap . :normal .<CR>

nnoremap <leader>z me%mw%r `wx`e

nnoremap Y y$
nnoremap z %
omap z %
vmap z %

"Paste from the yank register (pipe needs to be escaped, backslash doesn't)
nnoremap \ "0p
nnoremap \| "0P

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
nnoremap <leader>j :%!python -mjson.tool<CR>

" Format Elm
"nnoremap <leader>e :%!elm-format --stdin<CR>
nnoremap <leader>e mo:%!elm-format --stdin<CR>`o

" Compile Coffee
vmap <leader>c <esc>:'<,'>:CoffeeCompile<CR>
map <leader>c :CoffeeCompile<CR>
command -nargs=1 C CoffeeCompile | :<args>

" unescape \n in logs
nnoremap <leader>n :%s/\\n/\r/g<CR>

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

map <silent> <F5> :python exaltedDot(False)<CR>
map <silent> <F6> :python exaltedDot(True)<CR>


"==============================================================
" COMMENTS

function! MultiComment(after_spaces)
      if 0
  elseif &filetype == 'haskell' | let c = '-- '
  elseif &filetype == 'elm' | let c = '-- '
  elseif &filetype == 'javascript' | let c = '\/\/'
  elseif &filetype == 'jade' | let c = '\/\/'
  elseif &filetype == 'vim' | let c = '"'
  else | let c = '#'
  endif

  let s = a:after_spaces ? "\\(\\s*\\)" : ""

  execute "s/^".s."/\\1".c."/"
  execute "s/^".s.c.c."/\\1/e"
endfunction

" backspace comments
map <silent> <BS> :call MultiComment(0)<CR>+


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


"nnoremap <silent> * normal! * | :let @/ = "\\C" . @/<cr>



"===============================================================
" BUFFERS and WINDOWS
"
set hidden

nnoremap ' <C-w>w

"save position on old buffer, change buffer, move to saved position on new buffeer
nnoremap <silent> <C-L> mt:bnext<CR>`t
nnoremap <silent> <C-H> mt:bprev<CR>`t

"===============================================================
" GIT
"
map <leader>l :Glog<CR>
map <leader>b :Gblame<CR>
vmap <leader>b <esc>:'<,'>:Gblame<CR>

