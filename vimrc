
set nocompatible               " be iMproved


" Vundle stuff
filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
Bundle 'gmarik/vundle'



" general
set wildmode=longest,list
set nocompatible
set scrolloff=3
"highlight Normal ctermfg=grey ctermbg=black

map  <F2> :w<CR>
map! <F2> <ESC>:w<CR>a

"map <C-l> :tabn<Return>
"map <C-h> :tabp<Return>
"map <C-0> :tabnew 







set tabstop=2
set softtabstop=2
set shiftwidth=2
set textwidth=80
set smarttab
set expandtab



" search
set incsearch
set ignorecase
set smartcase



" autocommands
autocmd BufWrite	*.rb,*.py,*.sh	!chmod +x %



" bundles - multifile {{{
  Bundle 'vim-scripts/minibufexpl.vim'
  " {{{
    let g:miniBufExplVSplit             = 25 " vertical explorer, 25 col width
    let g:miniBufExplSplitBelow         = 1  " new windows go bottom or right
    let g:miniBufExplorerMoreThanOne    = 2  " 2 buffers to activate mbe
    nmap <leader>b :MiniBufExplorer<cr>
  " }}}

  Bundle 'kien/ctrlp.vim'
  " {{{
    let g:ctrlp_cache_dir = '/tmp/ctrlp-cache'
    nnoremap <silent> <leader>e :CtrlP<cr>
  " }}}

  Bundle 'vim-scripts/bufkill.vim'
  Bundle 'mileszs/ack.vim'
  " {{{
    let g:ackprg="ack -H --nocolor --nogroup --column"
  " }}}
" }}}

" bundles - editing {{{
  Bundle 'godlygeek/tabular'
  " {{{
    if exists(":Tabularize")
      vmap <leader>a= :Tabularize /=<CR>
      vmap <leader>a; :Tabularize /:\zs<CR>
    endif
  " }}}

  Bundle 'tpope/vim-surround'
" }}}

" bundles - languages {{{
  Bundle 'scrooloose/syntastic'
    " {{{
      let g:syntastic_check_on_open   = 1
      let g:syntastic_enable_balloons = 0
      nmap <leader>c :SyntasticCheck<cr>
    " }}}
"""  Bundle 'fs111/pydoc.vim'
"""  " {{{
"""    let g:pydoc_open_cmd = "tabnew"
"""    let g:pydoc_cmd      = "python -m pydoc"
"""  " }}}
  Bundle 'vim-scripts/mako.vim'
  Bundle 'kchmck/vim-coffee-script'
  Bundle 'tpope/vim-haml'
" }}}

" bundles - look {{{
"  Bundle 'vim-scripts/two2tango'
"  Bundle 'altercation/vim-colors-solarized'
  " {{{
"    if &t_Co > 2 || has("gui_running")
"      colorscheme two2tango
"    endif
    " if has("gui_running")
    "   set background=light
    " else
    "   set background=dark
    " endif
  " }}}
" }}}

filetype plugin indent on     " required!
syntax enable

" system {{{
  set title         " control window/terminal title
  set nobackup      " don't backup on overwrite
  set nowritebackup " ditto

  " - double '//' means complete path to swap file is preserved,
  "   but with % signs replacing '/'
  " - if the ~/.vim/tmp directory is not available, fallback to same
  "   directory as edited file
  set directory=$HOME/.vim/tmp//,.
"  set shell=/bin/zsh
" }}}

" look {{{
  set number     " display line numbers
  set ruler      " display cursor position
  set showmode   " display current mode
  set showcmd    " display useful information on last line
  set cursorline " highlight current line

"   statusline {{{
    set laststatus=2
    set statusline=
    set statusline+=%-3.3n\                          " buffer number
    set statusline+=%f\                              " filename
    set statusline+=%h%m%r%w                         " status flags: help,
"modified, readonly, preview
    set statusline+=\[%{strlen(&fenc)?&fenc:'none'}] " file encoding
    set statusline+=\[%{strlen(&ft)?&ft:'none'}]     " file type
    set statusline+=%=                               " right align remainder
    set statusline+=0x%-8B                           " character value
    set statusline+=%-14(%l,%c%V%)                   " line, character
    set statusline+=%<%P                             " file position
"   }}}
" }}}

" feel - alerts {{{
set noerrorbells visualbell t_vb=
if has('autocmd')
  autocmd GUIEnter * set visualbell t_vb=
endif
" }}}

" feel - buffers {{{
  set hidden " allow switching buffers without saving

  " - wild {{{
  "     first <tab>: list:longest
  "     When more than one match, list all matches and
  "     complete till longest common string.

  "     subsequent <tab>s: full
  "     complete next full match
  " }}}
  set wildmenu
  set wildmode=list:longest,full
  set wildignore=*.o,*.pyc,*.hi
" }}}
" feel - search {{{
  set ignorecase
  set smartcase
  set hlsearch
  set incsearch
" }}}
" feel - whitespace {{{
  set tabstop=2
  set shiftwidth=2
  set expandtab                       " spaces > tabs
  set smarttab
  set autoindent
  set smartindent
  set backspace=indent,eol,start      " enable backspace as often as possible
  set list                            " Show trailing spaces and tabs
  set listchars=tab:▸⋅,trail:⋅,nbsp:⋅ " What to show
" }}}

" Keybinds - overrides {{{
nnoremap Y y$
nmap K <Nop>
vmap K <Nop>
map Q <Nop>
map ` <Nop>
vnoremap < <gv
vnoremap > >gv
" }}}
" Keybinds - windows {{{
map <M-j> <C-w>j
map <M-k> <C-w>k
map <M-h> <C-w>h
map <M-l> <C-w>l
" }}}
nmap <leader><CR> o<Esc>
" Keybinds - leaders {{{
"   vimrc manipulation {{{
    nmap <silent> <leader>lv :e $HOME/.vimrc<CR>
    nmap <silent> <leader>sv :so $HOME/.vimrc<CR>
"   }}}
"   system clipboard {{{
    map <leader>y "*y
    map <leader>p "*p
"   }}}
"   buffer switching {{{
    nnoremap <leader><space> :b#<CR> " most recent buffer
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
"   }}}
" Keybinds - misc {{{
    map <leader>l :nohlsearch<CR>
"   }}}
" }}}

map <leader>ws :%s/\s\+$//g<CR>

" languages - python {{{
  " from http://dev.pocoo.org/hg/mitsuhiko-dotvim
  autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=8
  \ formatoptions+=croq softtabstop=4 smartindent
  \ cinwords=if,elif,else,for,while,try,except,finally,def,class,with

  let python_highlight_all        = 1
  let python_highlight_exceptions = 0
  let python_highlight_builtins   = 0
" }}}

" Add the virtualenv's site-packages to vim path
py << EOF
import os.path
import sys
import vim
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    sys.path.insert(0, project_base_dir)
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF

