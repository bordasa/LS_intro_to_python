info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_split = info.split(':')

new_info = '+'.join(info_split)
print(new_info)