from cc3d.cpp import CompuCell

# IMPORTANT: It is best to always provide hand-written iterators for STL
# containers even though swig generates them for you.
# with multiple swig modules  those autogenerated iterators will work on one platform and crash on another
# ones so best solution is to write iterators yourself

# this is used to iterate more easily over cells

class CellList:
    def __init__(self, inventory):
        self.inventory = inventory

    def __iter__(self):
        return CellListIterator(self)

    def __len__(self):
        return int(self.inventory.getSize())


class CellListIterator:
    def __init__(self, cellList):
        self.next = self.__next__
        self.inventory = cellList.inventory
        self.invItr = CompuCell.STLPyIteratorCINV()
        self.invItr.initialize(self.inventory.getContainer())
        self.invItr.setToBegin()

    def __next__(self):
        if not self.invItr.isEnd():
            self.cell = self.invItr.getCurrentRef()
            self.invItr.next()
            return self.cell
        else:
            raise StopIteration

    def __iter__(self):
        return self


#########################################################################
# iterating over inventory of cells of a given type
class CellListByType:
    def __init__(self, _inventory, *args):
        self.inventory = _inventory

        self.types = CompuCell.vectorint()

        self.inventoryByType = CompuCell.mapLongCellGPtr()

        self.initTypeVec(args)
        self.inventory.initCellInventoryByMultiType(self.inventoryByType, self.types)

    def __iter__(self):
        return CellListByTypeIterator(self)

    def __call__(self, *args):
        self.initTypeVec(args)
        self.inventory.initCellInventoryByMultiType(self.inventoryByType, self.types)

        return self

    def __len__(self):
        return int(self.inventoryByType.size())

    def initTypeVec(self, _typeList):

        self.types.clear()
        if len(_typeList) <= 0:
            self.types.push_back(1)  # type 1
        else:
            for type in _typeList:
                self.types.push_back(type)

    def initializeWithType(self, _type):
        self.types.clear()
        self.types.push_back(_type)
        self.inventory.initCellInventoryByMultiType(self.inventoryByType, self.types)

    def refresh(self):
        self.inventory.initCellInventoryByMultiType(self.inventoryByType, self.types)


class CellListByTypeIterator:
    def __init__(self, _cellListByType):
        self.inventoryByType = _cellListByType.inventoryByType
        self.invItr = CompuCell.mapLongCellGPtrPyItr()
        self.invItr.initialize(self.inventoryByType)
        self.invItr.setToBegin()
        self.next = self.__next__

    def __next__(self):
        if not self.invItr.isEnd():
            self.cell = self.invItr.getCurrentRef()
            # print 'self.idCellPair=',self.idCellPair
            # print 'dir(self.idCellPair)=',dir(self.idCellPair)
            self.invItr.next()
            return self.cell
        #
        else:
            raise StopIteration

    def __iter__(self):
        return self



#########################################################################
# this is used to iterate more easily over clusters
class ClusterList:
    def __init__(self, _inventory):
        self.inventory = _inventory.getClusterInventory().getContainer()

    def __iter__(self):
        return ClusterListIterator(self)

    def __len__(self):
        return int(self.inventory.size())


class ClusterListIterator:
    def __init__(self, _cellList):
        self.inventory = _cellList.inventory
        self.invItr = CompuCell.compartmentinventoryPtrPyItr()
        self.invItr.initialize(self.inventory)
        self.invItr.setToBegin()
        self.compartmentList = None
        self.next = self.__next__

    def __next__(self):

        if not self.invItr.isEnd():
            self.compartmentList = self.invItr.getCurrentRef()
            self.invItr.next()
            return self.compartmentList
        #
        else:
            raise StopIteration


# this is used to iterate more easily over clusters and avoid strange looking Python syntax

class Clusters:
    def __init__(self, _inventory):
        self.inventory = _inventory.getClusterInventory().getContainer()

    def __iter__(self):
        return ClustersIterator(self)

    def __len__(self):
        return int(self.inventory.size())


class ClustersIterator:
    def __init__(self, _cellList):

        self.next = self.__next__
        self.inventory = _cellList.inventory

        self.invItr = CompuCell.compartmentinventoryPtrPyItr()
        self.invItr.initialize(self.inventory)
        self.invItr.setToBegin()

        self.compartmentList = None

    def __next__(self):

        if not self.invItr.isEnd():
            self.compartmentList = self.invItr.getCurrentRef()
            # print 'self.idCellPair=',self.idCellPair
            # print 'dir(self.idCellPair)=',dir(self.idCellPair)
            self.invItr.next()
            return CompartmentList(self.compartmentList)
        #
        else:
            raise StopIteration


# this is used to iterate more easily over list of compartments , notice regular map iteration will work too but this is more abstracted out and will work with other containers too

class CompartmentList:
    def __init__(self, _inventory):
        self.inventory = _inventory

    def __iter__(self):
        return CompartmentListIterator(self)

    def __len__(self):
        return int(self.inventory.size())

    def clusterId(self):
        return self.__iter__().next().clusterId

class CompartmentListIterator:
    def __init__(self, _cellList):
        self.next = self.__next__
        self.inventory = _cellList.inventory
        self.invItr = CompuCell.mapLongCellGPtrPyItr()
        self.invItr.initialize(self.inventory)
        self.invItr.setToBegin()

    def __next__(self):
        if not self.invItr.isEnd():
            self.cell = self.invItr.getCurrentRef()
            # print 'self.idCellPair=',self.idCellPair
            # print 'dir(self.idCellPair)=',dir(self.idCellPair)
            self.invItr.next()
            return self.cell
        #
        else:
            raise StopIteration

    def __iter__(self):
        return self

# this is wrapper for std::vector<CellG*>
class ClusterCellList:
    def __init__(self, _inventory):
        self.inventory = _inventory

    def __iter__(self):
        return ClusterCellListIterator(self)

    def __len__(self):
        return int(self.inventory.size())


class ClusterCellListIterator:
    def __init__(self, _cellList):
        self.next = self.__next__
        self.inventory = _cellList.inventory
        # print "dir(self.inventory)=",dir(self.inventory)
        self.currentIdx = 0
        self.cell = None
        # self.invItr.initialize(self.inventory.getContainer())
        # self.invItr.setToBegin()

    def __next__(self):
        # if self.invItr !=  self.inventory.end():
        if self.currentIdx < self.inventory.size():
            # print "self.invItr=",dir(self.invItr)
            # print "self.invItr.next()=",self.invItr.next()
            # self.compartmentList = self.invItr.next()



            self.cell = self.inventory[self.currentIdx]
            self.currentIdx += 1

            return self.cell
        else:
            raise StopIteration

    def __iter__(self):
        return self

    # legacy code  - do not modify
