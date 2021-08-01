def tail(file_path, read_line=10)
  current_bite = 0
  file = File.open(file_path.to_s)
  file.seek(current_bite, IO::SEEK_END)
  indention_count = read_line + 1

  until indention_count.zero?
    current_bite -= 1
    begin
      file.seek(current_bite, IO::SEEK_END)
      indention_count -= 1 if file.getc == "\n"
    rescue
      file.seek(0)
      break
    end
  end
  file.each.to_a
end
