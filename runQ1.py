import os

c1="g++ -c main.cpp"
c2="g++ main.o -o sfml-app -pthread -lsfml-graphics -lsfml-window -lsfml-system"
c3="./sfml-app"
print(c1)
os.system(c1)
print(c2)
os.system(c2)
print(c3)
os.system(c3)
