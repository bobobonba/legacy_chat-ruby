#! /usr/bin/ruby

print "Content-Type: text/html; charset=UTF-8\n\n"

require 'cgi'

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

latest_log = chat_log.reverse_each.with_index.map do |text, index|
  if index > 100
    exit
  else
    text
  end
end

latest_log.reverse.each do |text|
  print cgi.div{ text } 
end

print <<EOF
  <form action="write.cgi" method="get">
    <input type="text" name="text_area">
    <input type="submit" value="書き込む">
  </form> 
EOF

print <<EOF
</body>
</html>
EOF