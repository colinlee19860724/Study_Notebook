" 大括号 { 仅表示功能区，属于注释的一部分，无其他含义
syntax on                   "语法支持

"common conf {{             通用配置
set helplang=cn             "帮助系统设置为中文
set autoindent              "自动缩进
set bs=2                    "在insert模式下用退格键删除
set showmatch               "代码匹配
set laststatus=2            "总是显示状态行
set expandtab               "以下三个配置配合使用，设置tab和缩进空格数
set shiftwidth=4            "自动缩进所使用的空白长度
set tabstop=4               "定义tab所等同的空格长度
"set cursorline              "为光标所在行加下划线
set number                  "显示行号
set relativenumber          "显示相对行号
set autoread                "文件在Vim之外修改过，自动重新读入
set ignorecase              "检索时忽略大小写
set fileencodings=uft-8,gbk "使用utf-8或gbk打开文件
set hls                     "检索时高亮显示匹配项
set foldmethod=syntax       "代码折叠
"}}

" conf for tabs, 为标签页进行的配置，通过ctrl h/l切换标签等
let mapleader = ','
nnoremap <C-l> gt
nnoremap <C-h> gT
nnoremap <leader>t : tabe<CR>

"conf for plugins {{ 插件相关的配置
"状态栏的配置 
"powerline{
set guifont=PowerlineSymbols\ for\ Powerline
set nocompatible
set t_Co=256
let g:Powerline_symbols = 'fancy'
"}

"pathogen是Vim用来管理插件的插件
"pathogen{
"	call pathogen#infect()
"}

"}}

" 自动为 shell 文件加上版权信息
autocmd BufNewFile *.sh exec ":call SetTitle()"
func SetTitle()
	if expand("%:e") == 'sh'
	call setline(1,"#!/bin/bash") 
	call setline(2,"#") 
	call setline(3,"#********************************************************************") 
	call setline(4,"#Author:		ColinLee") 
	call setline(5,"#QQ: 			517999276") 
	call setline(6,"#Date: 			".strftime("%Y-%m-%d"))
	call setline(7,"#FileName：		".expand("%"))
	call setline(8,"#URL: 			https://github.com/colinlee19860724")
	call setline(9,"#Description：		I may write it later.") 
	call setline(10,"#Copyright (C): 	".strftime("%Y")." All rights reserved")
	call setline(11,"#********************************************************************") 
	call setline(12,"") 
	endif
endfunc
autocmd BufNewFile * normal G
