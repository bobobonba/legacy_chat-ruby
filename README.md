# legacy_chat-ruby

## 起動手順

1.
```
$ docker build -t ruby_cgi .
```
2.
```
$ docker run -v $PWD/www:/var/www/html -it -p 8080:80 ruby_cgi
```
