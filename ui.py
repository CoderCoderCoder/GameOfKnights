#!/usr/bin/python
class UI(object):
  def getInput(self, inputQuestion):
    pass
  
  def __printMenu(self,dOptionToFunction):
    dKeyToOption = dict()
    iCnt = 0
    for sCurOption in dOptionToFunction.keys():
      dKeyToOption[str(iCnt)] = sCurOption
      print "%d for %s"%(iCnt, sCurOption)
      iCnt+=1
    return dKeyToOption
      
  def menu(self, dOptionToFunction):
    """A menu that displays a set of options and maps their selection to functions.
    The parameter dOptionToFunction contains tuples of the form ("value", func).
    If func is not callable, then it is returned as a value. If it is callable, then 
    the returned value of the call is returned from the menu.
    """
    dKeyToOption = self.__printMenu(dOptionToFunction)
    
    sResp = raw_input()
    while not (sResp in dKeyToOption.keys()):
      print "\nWARNING: INVALID OPTION\nPlease select a valid option (From zero to %d)."%(len(dKeyToOption) - 1)
      dKeyToOption = self.__printMenu(dOptionToFunction)
      sResp = raw_input()

    try:
      return dOptionToFunction[dKeyToOption[sResp]]()
    except:
      return dOptionToFunction[dKeyToOption[sResp]]
    
  
if __name__ == "__main__":
  import sys
  ui = UI()
  ui.menu({"Test1" : lambda : sys.stdout.write("1 run!\n"),
	   "Test2" : lambda : sys.stdout.write("2 run!\n"),
	   "Exit": lambda: None})
