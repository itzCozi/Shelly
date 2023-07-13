# Made for cruelty squad's .save files
import os, sys
import time


def parseSave(file_path):
  if not os.path.exists(file_path):
    raise FileNotFoundError('Given file path does not exist')
  else:
    with open(file_path, 'r') as r:
      lines = r.read().split(',')
      r.close()

  for line in lines: # Its messy ik i made it at 1 today...
    if '}' in line:
      linenum = lines.index(line)  # Get current line's number relitive to list
      linelist = list(lines[linenum])
      index = lines[linenum].find('}')  # get the index of '}' 
      linelist.insert(index, '\n')  # Insert a newline before the index
      # Then update the list
      lines.remove(line) ; lines.insert(linenum, ''.join(linelist)) ; line = ''.join(linelist) 
    if '{' in line:
      linenum = lines.index(line)
      linelist = list(lines[linenum])
      index = lines[linenum].find('{')
      linelist.insert(index+1, '\n')
      lines.remove(line) ; lines.insert(linenum, ''.join(linelist)) ; line = ''.join(linelist) 
    if ':' in line:
      linenum = lines.index(line)
      linelist = list(lines[linenum])
      index = lines[linenum].find(':')
      linelist.insert(index+1, ' ')
      lines.remove(line) ; lines.insert(linenum, ''.join(linelist)) ; line = ''.join(linelist) 
    if '[' in line:
      Qstart = lines.index(line)
      
      linenum = lines.index(line)
      linelist = list(lines[linenum])
      index = lines[linenum].find('[')
      linelist.insert(index+1, '\n  ')
      lines.remove(line) ; lines.insert(linenum, ''.join(linelist)) ; line = ''.join(linelist) 
    if ']' in line:
      Qend = lines.index(line)
      # This indents every line in a bracket
      if 'Qend' and 'Qstart' in locals():
        for line1 in lines[Qstart+1:Qend]:
          line1num = lines.index(line1)
          lines.remove(line1)
          line1 = '  ' + line1
          lines.insert(line1num, line1)
      
      linenum = lines.index(line)
      linelist = list(lines[linenum])
      index = lines[linenum].find(']')
      linelist.insert(index, '\n')
      linelist.insert(0, '  ')
      lines.remove(line) ; lines.insert(linenum, ''.join(linelist)) ; line = ''.join(linelist)

  print('\n'.join(lines))
      
parseSave('Cruelty Squad/savegame.save')