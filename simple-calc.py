"""
KALKULATOR

Module : curses
windows
    $ pip install windows-curses
linux
    # apt-get install libncurses-dev

================================

=> 10+28

      <-  C   *
  7   8   9   /
  4   5   6   +
  1   2   3   -
      0   .   =
"""

import curses


def main(stdscr):
  curses.curs_set(0)
  curses.mousemask(curses.ALL_MOUSE_EVENTS)

  stdscr.clear()
  stdscr.refresh()

  btn_px = 2
  btn_py = 3
  btn_gx = 3
  btn_gy = 1

  btn_list = [
      # label, index row, index col
      (" ", 0, 0), ("<-", 0, 1), ("C", 0, 2), ("*", 0, 3),
      ("7", 1, 0), ("8", 1, 1),  ("9", 1, 2), ("/", 1, 3),
      ("4", 2, 0), ("5", 2, 1),  ("6", 2, 2), ("+", 2, 3),
      ("1", 3, 0), ("2", 3, 1),  ("3", 3, 2), ("-", 3, 3),
      (" ", 4, 0), ("0", 4, 1),  (".", 4, 2), ("=", 4, 3)
  ]

  for label, row, col in btn_list:
    x = btn_px + col + (btn_gx * col)
    y = btn_py + row + (btn_gy * row)
    stdscr.addstr(y, x, label)

  stdscr.refresh()

  disp_text = ""

  while True:
    stdscr.move(0, 0)
    stdscr.clrtoeol()
    stdscr.addstr(0, 0, "=> " + disp_text)
    stdscr.refresh()

    key = stdscr.getch()

    if key == ord('q'):
      break

    if key == curses.KEY_MOUSE:
      try:
        _, mx, my, _, _ = curses.getmouse()

        for label, row, col in btn_list:
          x = btn_px + col + (btn_gx * col)
          y = btn_py + row + (btn_gy * row)

          if mx == x and my == y:
            if label == " ":
              break
            elif label == "C":
              disp_text = ""
            elif label == "<-":
              disp_text = disp_text[:-1]
            elif label == "=":
              disp_text = str(eval(disp_text))
            else:
              disp_text += label

            break
      except curses.error:
        pass


curses.wrapper(main)
