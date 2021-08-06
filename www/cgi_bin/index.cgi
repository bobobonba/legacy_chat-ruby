#! /usr/bin/ruby

require 'cgi'
require 'json'
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

chat_log = File.open('./log/chat_log.json', 'r')
cgi = CGI.new('html4')

latest_log = tail('./log/chat_log.json', 100)
latest_log.each do |json|
  json_hash = JSON.parse(json.to_s)

  print cgi.div{ json_hash['date'].to_s }
  print cgi.div{ json_hash['text'].to_s }
  print cgi.br
end

print <<EOF
  <form onsubmit="return false;" action="write.cgi" method="post">
    <input type="text" name="text_area" autofocus>
    <input type="button" value="書き込む" onclick="submit(); disabled=true;">
  </form>
EOF

print <<EOF
</body>
</html>
EOF
