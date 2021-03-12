colorscheme jellybeans

" delimitMate
let delimitMate_expand_cr=1


set ai
set si
set shiftwidth=4
set tabstop=3
syntax on
set nocompatible

filetype indent on
filetype on
filetype plugin on

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
" vim-airline
"VundleVim/Vundle.vim
Plugin 'gmarik/Vundle.vim'
"After install YouCompleteMe

Plugin 'edkolev/promptline.vim'

Plugin 'Raimondi/delimitMate'

Plugin 'bling/vim-airline'

"PreInstalled Markdown Plugin
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
"After install jedi-vim
"After install NERDTree plugin
Plugin 'scrooloose/nerdtree'
Plugin 'Xuyuanp/nerdtree-git-plugin'
call vundle#end()
filetype plugin indent on

syntax on
colo jellybeans
set nu
set mouse=a
set tabstop=2

"au VimEnter * NERDTree
