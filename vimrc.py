# coding=utf-8

import vim

def exaltedDot(add):

  row, col = vim.current.window.cursor
  line = [None] + list(vim.current.buffer[row-1]) + [None]
  col += 1

  try: pair = (p for p in ['xo', 'XO', u'●○'] if line[col] in p).next()
  except: return

  full, empty = list(pair)

  while line[col] == full: col += 1
  while line[col-1] == empty: col -= 1

  if add:
    if line[col] == empty: line[col] = full
  else:
    if line[col-1] == full: line[col-1] = empty

  vim.current.buffer[row-1] = ''.join(line[1:-1])

