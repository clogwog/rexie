CXXFLAGS=-Wall -O3 -g -fno-strict-aliasing
BINARIES=rexie

RGB_INCDIR=include
RGB_LIBDIR=lib
LDFLAGS+=-L$(RGB_LIBDIR) -lrgbmatrix -lrt -lm -lpthread

all : $(BINARIES)


rexie : rexie.o $(RGB_LIBRARY)
	$(CXX) $(CXXFLAGS) rexie.o -o $@ $(LDFLAGS)


%.o : %.cpp
	$(CXX) -I$(RGB_INCDIR) $(CXXFLAGS) -DADAFRUIT_RGBMATRIX_HAT -c -o $@ $<

clean:
	rm -f *.o $(OBJECTS) $(BINARIES)

