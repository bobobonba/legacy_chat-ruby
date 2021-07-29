#! /usr/bin/ruby

print "Content-type:text/html;charset=UTF-8\n\n"

require 'cgi'

cgi = CGI.new('html4')
message = cgi['text_area']

File.open('./log/chat_log.txt', 'a+'){|file|
  file.write(message + "\n")
}

print cgi.h1{ '書き込みが完了しました' }
print cgi.a('index.cgi'){ 'チャットルームに戻る' }
