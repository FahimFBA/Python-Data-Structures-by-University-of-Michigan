{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. What is the difference between a Python tuple and Python list?\n",
    "    - Lists are mutable and tuples are not mutable\n",
    "2. Which of the following methods work both in Python lists and Python tuples?\n",
    "    - index()\n",
    "3. What will end up in the variable y after this code is executed? x , y = 3, 4\n",
    "    - 4\n",
    "4. In the following Python code, what will end up in the variable y? x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}; y = x.items()\n",
    "    - A list of tuples\n",
    "5. Which of the following tuples is greater than x in the following Python sequence? x = (5, 1, 3); if ??? > x : ...\n",
    "    - (6, 0, 0)\n",
    "6. What does the following Python code accomplish, assuming the c is a non-empty dictionary? tmp = list(); for k, v in c.items(): tmp.append( (v, k))\n",
    "    - It creates a list of tuples where each tuple is a value, key pair\n",
    "7. If the variable data is a Python list, how do we sort it in reverse order?\n",
    "    - data.sort(reverse=True)\n",
    "8. Using the following tuple, how would you print 'Wed'? days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')\n",
    "    - print days[2]\n",
    "9. In the following Python loop, why are there two iteration variables (k and v)? c = {'a':10, 'b':1, 'c':22}; for k, v in c.items() : ...\n",
    "    - Because the items() method in dictionaries returns a list of tuples\n",
    "10. Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?\n",
    "    - For a temporary variable that you will use and discard without modifying"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}