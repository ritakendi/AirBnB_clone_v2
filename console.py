#!/usr/bin/python3
""" console that contains the entry point """

import cmd  # test
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """ The console for AirBnB,
    written by Peter Wu and Bryan Leung """

    prompt = "(hbnb) "  # the intranet's required prompt
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]  # for tasks 8/ 9

    def do_quit(self, line):  # getting rid of parameters throws errors
        """Quit command to exit the program
        """
        exit()  # not sure if there is a desired return value
        # This expects a return True but for now, exit works just fine.

    def do_EOF(self, line):
        """ EOF calls on quit """
        print()  # for a new line
        exit()  # assuming EOF function does the same as do_quit

    def emptyline(self):
        """ do nothing """
        pass  # will get a new line and aprompt

    # The above is for Console 0.0.1
    # Below is for Console 0.1 or task 7 and onwards

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves to a JSON file,
        and prints the ID when finished """

        if len(line) < 1:  # if no arguments passed
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")  # if class doesn't exist
        else:
            new = eval(line)()  # execute the string argument into a shell
            print(new.id)  # prints the new id of the object we created
            new.save()  # serialize into JSON file

    def do_show(self, line):  # shows the class and id
        """ Prints the string representation of an instance,
        if given the class name and id """

        classID = ""  # will store the input if >= 2 words
        if len(line) < 1:  # user just typed show into CLI
            print("** class name missing **")
            return  # not sure if we need a return value?
        tokenize = shlex.split(line)  # tokenize the input with split
        if tokenize[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")  # they typed a fake class
        elif len(tokenize) < 2:  # user typed a class with no ID
            print("** instance id missing **")
        else:  # we have 2 or more arguments now. should unit test this
            classID = tokenize[0] + "." + tokenize[1]
            # combines the 2 strings- class with the id
            if classID in storage.all().keys():
                print(storage.all()[classID])  # prints the object!!
            # matching class and id is found in our storage, success!!!
            else:
                print("** no instance found **")  # bad

    def do_destroy(self, line):
        """ Deletes an instance of an object if given
        the class name and the ID. Then save the changes """

        # pretty much exactly like do_show but add a del()
        # lollll i just copy pasted the above
        classID = ""
        if len(line) < 1:
            print("** class name missing **")
            return  # not sure if we need a return value?
        tokenize = shlex.split(line)
        if tokenize[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")  # they typed a fake class
        elif len(tokenize) < 2:  # user typed a class with no ID
            print("** instance id missing **")
        else:  # we have 2 or more arguments now. should unit test this
            classID = tokenize[0] + "." + tokenize[1]
            # combines the 2 strings- class with the id
            if classID in storage.all().keys():
                del storage.all()[classID]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, line):
        """ Prints a string of all instances or if given the class name,
        of just the instances of the class name """
        # print all values in the storage.all() if no paremeters entered
        # otherwise print only values that match parameters entered
        if (len(line) < 1):
            print(["{}".format(v) for k, v in storage.all().items()])
        # print all instances but does not print empty brackets if empty
        else:  # first check if the class is in our list of classes
            tokenize = shlex.split(line)
            if tokenize[0] not in self.classes:
                print("** class doesn't exist **")
            else:  # print everything we have
                print(["{}".format(v) for k, v in storage.all().items()
                       if type(v).__name__ in tokenize[0]])

    def do_update(self, line):
        """ Updates an instance based on the class name and ID.
        Adds or updates attributes ans saves the changes """
        # TOO MANY WORDS
        # lots of same checks for line lenths and error messages,
        # should expect a str len of 4.
        # 0 is class, 1 is id, 2 is attr, 3 is value.
        # try an if or try in case arguments are bad?!?!
        if len(line) < 1:
            print("** class name missing **")
        else:  # just number of arguments checking
            tokenize = shlex.split(line)
            if len(tokenize) == 3:
                print("** value missing **")
            elif len(tokenize) == 2:
                print("** attribute name missing **")
            elif len(tokenize) == 1:
                print("** instance id missing **")
            else:  # of arguments is correct, now check if class exists
                if tokenize[0] not in self.classes:
                    print("** class doesn't exist **")
                else:  # check if the id exists
                    key = tokenize[0] + "." + tokenize[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:  # we have a match! now check the data types
                        obj = storage.all().get(key, 0)
                        try:  # we will try to set attr
                            setattr(obj, tokenize[2], type(getattr(obj,
                                    tokenize[2]))(tokenize[3]))
                        except AttributeError:  # the attr data type is bad
                            try:  # try with int casting, it it works yey
                                val = int(tokenize[3])
                            except ValueError:
                                try:  # try with float cause int didnt work
                                    val = float(tokenize[3])
                                except ValueError:
                                    val = str(tokenize[3])  # try with str
                            setattr(obj, tokenize[2], val)  # set attribute
                        storage.save()  # save the object to storage

    def do_count(self, line):
        """ counts number of objects of specified class """
        if len(line) < 1:  # checks id there is a class name
            print("** class name missing **")
        else:  # We split the input and if class given exists
            tokenize = shlex.split(line)
            if tokenize[0] not in self.classes:
                print("** class doesn't exist **")
            else:  # we have a counter now for each class
                cnt = 0
                obj = storage.all()  # obj is our data storage
                for k, v in obj.items():  # this increases our counter
                    if type(v).__name__ == tokenize[0]:
                        cnt += 1  # by matching all class names
                print(cnt)

    def default(self, line):
        """default when user type in class using <class name>.all()"""
        methods = {"all": self.do_all, "count": self.do_count,
                   "show": self.do_show, "destroy": self.do_destroy,
                   "update": self.do_update}
        # we have a dict for the advance problems. we already coded the
        # basic functionalities the advance problems require. so we will just
        # redirect and call on those functions that we have made.
        # Peter did this part. he did a lot of string manipulation with . as
        # a delimiter but i would have tried to add . as a white space
        # attribute in the shlex arguments.
        key = line.split(".")
        if len(key) < 2:
            print("** missing arguments **")
        else:  # lol peter did some crazy string manipulation
            subkey = key[1].split("(")
            if subkey[0] not in methods:
                print("** invalid command **")
            else:
                subkey[1] = subkey[1].replace(")", "")
                if "{" in subkey[1]:
                    subkey[1] = subkey[1].replace(',', ':', 1)
                    t = '{' + subkey[1] + '}'
                    t = t.replace("'", '"')
                    d = {}
                    try:
                        d = json.loads(t)
                    except:
                        print("** invalid format **")
                        return
                    for k, v in d.items():
                        for k1, v1 in v.items():
                            ustr = ""
                            ustr = key[0] + " " + k + " " + k1 + " " + str(v1)
                            methods[subkey[0]](ustr)
                else:
                    subkey[1] = subkey[1].replace(",", " ")
                    methods[subkey[0]](key[0] + " " + subkey[1])


if __name__ == "__main__":
    # protects against execution when imported
    HBNBCommand().cmdloop()  # recursively loops back until exited or errors
