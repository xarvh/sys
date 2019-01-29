"===============================================================
" GENERAL
"

"call plug#begin('~/.vim/plugged')
"
"Plug 'elmcast/elm-vim'
"Plug 'tpope/vim-fugitive'
"Plug 'tpope/vim-vinegar'
"Plug 'mileszs/ack.vim'
"Plug 'vim-airline/vim-airline'
"Plug 'scrooloose/syntastic'

"call plug#end()



"let g:syntastic_always_populate_loc_list = 1
"let g:syntastic_auto_loc_list = 1
"let g:elm_syntastic_show_warnings = 1

"let g:deoplete#omni_patterns.elm = '\.'
let g:elm_detailed_complete = 1

nnoremap - :E<CR>

"===============================================================
" GENERAL
"

let mapleader = ' '
set mouse=a
set directory=$HOME/.vim/tmp   " put swapfiles away

set clipboard+=unnamedplus
"set shortmess=atI

set scrolloff=3
"set wildmode=longest,list
"set textwidth=0


nnoremap <CR> :
"nnoremap <F9> :source $MYVIMRC<CR>
filetype plugin on
filetype indent on


"===============================================================
" APPEARANCE
"
set termguicolors
colorscheme darkblue
"set guioptions=acegi
"set gfn=Monospace\ Bold\ 11
"set cursorline
highlight CursorLine cterm=NONE ctermbg=darkblue
"
nnoremap <leader>w :set wrap!<CR>

"highlight TrailingWhitespace ctermbg=red guibg=red
"match TrailingWhitespace /\s\+$/


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
"nnoremap \ "0p
"nnoremap \| "0P

"==============================================================
" INDENTATION
"
set expandtab "insert spaces when Tab is pressed
set shiftwidth=2
"set tabstop=2
"set softtabstop=2
"set smarttab


"==============================================================
" LANGUAGE SPECIFICS
"
" Beautify JSON
nnoremap <leader>j :%!python -mjson.tool<CR>

" Format Elm
"nnoremap <leader>e :%!elm-format --stdin<CR>
nnoremap <leader>e mo:%!elm-format --stdin<CR>`o


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
set ignorecase
set smartcase
set gdefault "Use 'g' flag by default with :s/foo/bar/.

map <leader>f :AckFile!<space>
map <leader>a :Ack!<space>
map <leader>8 :Ack! <cword><CR>


"nnoremap <silent> * normal! * | :let @/ = "\\C" . @/<cr>



"===============================================================
" BUFFERS and WINDOWS
"
set hidden
nnoremap ' <C-w>w
nnoremap <C-L> :bnext<CR>
nnoremap <C-H> :bprev<CR>


"===============================================================
" GIT
"
map <leader>l :Glog<CR>
map <leader>b :Gblame<CR>
vmap <leader>b <esc>:'<,'>:Gblame<CR>

