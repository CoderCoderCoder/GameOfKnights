import random;
from traps import *;
from treasures import *;
from soldiers import *;
from towers import *;

class GameMap(object):
    def getInstanceOfTrap(self,  sClassName):
      return eval(sClassName +"()");
      
    def getInstanceOfTreasure(self,  sClassName):
      return eval(sClassName +"(self.economy, self)");
    
    def getInstanceOfFoe(self,  sClassName):
      return eval(sClassName +"(self.economy, self)");
    
    def __init__(self,  economy, xSize=10,  ySize=10, trapProbability=0.05, treasureProbability=0.05,  foeProbability =0.10,
		 towerProbability = 0.01):
        self.economy = economy;
        self.xSize = xSize;
        self.ySize = ySize;
        self.trapProbability = trapProbability;
        self.treasureProbability = treasureProbability;
        self.foeProbability = foeProbability;
        self.towerProbability = towerProbability;
        self.homePos = (0, 0);
    
        self.traps = [];
        self.treasures = [];
        self.foes = [];
        
        self.applyTraps();
        self.applyTreasures();
        self.applyFoes();
        
    def applyTraps(self, possibleTraps = ["Pit"]): #, "TrapClass", "ArrowSlit", "Explosion", "Labyrinth"]):
        # Apply traps
        self.traps = [];
        # Omit 0,0 because it is HOME
        for iCnt in range(1,  self.xSize): 
          for iCnt2 in range(1,  self.ySize):
	        if iCnt == self.homePos[0] and iCnt2 == self.homePos[1]:
	          continue # Do not put anything at home
          if (random.random() < self.trapProbability):
            curTrap = self.getInstanceOfTrap(random.choice(possibleTraps));
            curTrap.x = iCnt;
            curTrap.y = iCnt2;
        
            self.traps.append(curTrap);
          
          
    def applyTreasures(self, possibleTreasures = ["TreasureClass"]):#, "SmallTreasure", "BigTreasure", "HugeTreasure",
                  # "Ration", "SmallRation", "BigRation", "HugeRation",
                  # "Chest", "SmallChest", "BigChest", "HugeChest"
                  # ]):
        # Apply treasures
        for iCnt in range(0,  self.xSize): 
          for iCnt2 in range(0,  self.ySize):
	    if iCnt == self.homePos[0] and iCnt2 == self.homePos[1]:
	      continue # Do not put anything at home
            if (random.random() < self.treasureProbability):
              curTreasure = self.getInstanceOfTreasure(random.choice(possibleTreasures));
              curTreasure.x = iCnt;
              curTreasure.y = iCnt2;
          
              self.treasures.append(curTreasure);
          
    def applyFoes(self, possibleFoes = [ 
        # "AssassinClass",  "BarbarianClass",
#        "CartographerClass", 
      # "DruidClass",  
      # "EnchanterClass", 
      # "KnightClass",  
      "MageClass",  
      # "RangerClass", 
      "SoldierClass", 
      #  "TechnicianClass", 
#        "BridgeBuilderClass", 
      # "WizardClass",  
                  ],
      possibleTowers = ["FireElementalistTower",  "Fort", "TowerClass", 
        "IllusionistTower", "WaterElementalistTower",]):
        # Apply foes
        for iCnt in range(0,  self.xSize): 
          for iCnt2 in range(0,  self.ySize):
	    if iCnt == self.homePos[0] and iCnt2 == self.homePos[1]:
	      continue # Do not put anything at home
            if (random.random() < self.foeProbability):
              curFoe = self.getInstanceOfFoe(random.choice(possibleFoes));
              curFoe .x = iCnt;
              curFoe .y = iCnt2;
          
              self.foes.append(curFoe);
          
        # Apply foes
        for iCnt in range(0,  self.xSize): 
          for iCnt2 in range(0,  self.ySize):
	    if iCnt == self.homePos[0] and iCnt2 == self.homePos[1]:
	      continue # Do not put anything at home
            if (random.random() < self.towerProbability):
              curFoe = self.getInstanceOfFoe(random.choice(possibleTowers));
              curFoe .x = iCnt;
              curFoe .y = iCnt2;
          
              self.foes.append(curFoe);

    def getTraps(self, x, y):
      res = [];
      for curTrap in self.traps:
        if (curTrap.x == x and curTrap.y == y):
          res.append(curTrap);
          
      return res;
          
    def getTreasures(self, x, y):
      res = [];
      for curTreasure in self.treasures:
        if (curTreasure.x == x and curTreasure.y == y):
          res.append(curTreasure);
          
      return res;
      
    def getFoes(self, x, y):
      res = [];
      for curFoe in self.foes:
        if (curFoe.x == x and curFoe.y == y):
          res.append(curFoe);
          
      return res;
      