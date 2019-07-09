from matplotlib import pyplot as plt
import collections
import Custom_functions
from inspect import getmembers, isfunction

functions_list = [o for o in getmembers(Custom_functions) if isfunction(o[1])]
print(functions_list)

name_of_functions = []


def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return(getattr(module, name))


for tupl in functions_list:
    name = tupl[0]
    name_of_functions.append(name)
    _func = import_from("Custom_functions", name)
    vars()[name] = _func

# for func in name_of_functions:
#     print(func)
#     locals()[func](1, 1, 1)


class Custom_function:

    def exec_func(self, positionsdata, dicdistrelativedata, dicdistorigindata, func_name):
        self.result = globals()[self.func_name](self.positionsdata, self.dicdistrelativedata, self.dicdistorigindata)
        print("result", self.result)
        plt.figure()
        if len(self.result) > 2:
            try:
                self.title = self.result[2]
                self.xlabel = [3]
                self.ylabel = [4]
                plt.plot(self.x, self.y)
                plt.title("Absolute distance between points and origine")
                plt.xlabel("Frame")
                plt.ylabel("Distance (Px)")
            except:
                pass
        self.x = self.result[0]
        self.y = self.result[1]
        plt.plot(self.x, self.y)
        plt.show()

    def __init__(self, tk, root, func_name, menu, positionsdata, dicdistorigindata, dicdistrelativedata):
        self.positionsdata = positionsdata
        self.dicdistorigindata = dicdistorigindata
        self.dicdistrelativedata = dicdistrelativedata
        self.func_name = func_name
        self.tk = tk
        self.root = root
        self.menu = menu
        # self.selectplotmenu = tk.Menu(menu, tearoff=0)
        self.menu.add_command(label=func_name, command=lambda: self.exec_func(self.positionsdata, self.dicdistorigindata, self.dicdistrelativedata, self.func_name))
        # menu.add_cascade(label=name, menu=self.selectplotmenu)


class Dataset:

    def callback(self, name):
        pass

    def func_origine(self, positionsdata, dicdistorigindata):
        self.x = range(len(self.dicdistorigindata))
        self.y = self.dicdistorigindata
        print(self.y)
        plt.figure()
        plt.plot(self.x, self.y)
        plt.title("Absolute distance between points and origine")
        plt.xlabel("Frame")
        plt.ylabel("Distance (Px)")
        plt.show()

    def func_relative(self, positionsdata, dicdistrelativedata):
        self.x = range(len(self.dicdistrelativedata))
        self.y = self.dicdistrelativedata
        print(self.y)
        plt.figure()
        plt.plot(self.x, self.y)
        plt.title("Relative distance between points over time")
        plt.xlabel("Frame")
        plt.ylabel("Distance (Px)")
        plt.show()

    def func_gaussian(self, dicdistrelativedata):
        self.floored = [int(i) for i in dicdistrelativedata]
        self.c = collections.Counter(self.floored)
        print(self.c.keys())
        print(self.c.values())
        self.x = self.c.keys()
        self.y = self.c.values()
        plt.figure()
        plt.plot(self.x, self.y, 'o')
        plt.show()
        print(self.c)

    def __init__(self, tk, root, name, menu, dic, positionsdata, dicdistrelativedata, dicdistorigindata):
        self.tk = tk
        self.root = root
        self.menu = menu
        self.positionsdata = positionsdata
        self.name = name
        self.dicdistorigindata = dicdistorigindata
        self.dicdistrelativedata = dicdistrelativedata
        self.selectplotmenu = tk.Menu(menu, tearoff=0)
        self.selectplotmenu.add_command(label="Origine", command=lambda: self.func_origine(self.positionsdata, self.dicdistorigindata))
        self.selectplotmenu.add_command(label="Relative", command=lambda: self.func_relative(self.dicdistrelativedata, self.dicdistrelativedata))
        self.selectplotmenu.add_command(label="Gaussian", command=lambda: self.func_gaussian(self.dicdistrelativedata))
        menu.add_cascade(label=name, menu=self.selectplotmenu)

        dic[name] = 1

        for func in name_of_functions:
            print(000, func)
            Custom_function(self.tk, self.root, func, self.selectplotmenu, self.positionsdata, self.dicdistorigindata, self.dicdistrelativedata)
