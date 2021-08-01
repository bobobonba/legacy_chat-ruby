#! /usr/bin/ruby

require 'cgi'
require_relative 'file_utils.rb'

print "Content-Type: text/html; charset=UTF-8\n\n"
STDERR = STDOUT

print <<EOF 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>チャットルーム</title>
  </head>
  <body>
EOF

chat_log = File.open('./log/chat_log.txt', 'r')
cgi = CGI.new('html4')

latest_log = tail('./log/chat_log.txt', 100)
latest_log.each do |text|
  print cgi.div{ text }
end

print <<EOF
  <form action="write.cgi" method="get">
    <input type="text" name="text_area" autofocus>
    <input type="submit" value="書き込む">
  </form>
EOF

print <<EOF
</body>
</html>
EOF
