def make_readable(seconds):
    return '%02d:%02d:%02d' % (seconds / 60 / 60, seconds / 60 % 60, seconds % 60)


print make_readable(60)  # "00:01:00"
print make_readable(86399)  # "23:59:59"
