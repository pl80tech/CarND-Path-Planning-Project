project(Path_Planning)

cmake_minimum_required (VERSION 3.5)

add_definitions(-std=c++11)

# Add some options when running cmake
option(TEST1 "Enable Test 1" OFF)
option(TEST2 "Enable Test 2" OFF)
option(TEST3 "Enable Test 3" OFF)
option(TEST4 "Enable Test 4" OFF)
option(TEST5 "Enable Test 5" OFF)
option(TEST6 "Enable Test 6" OFF)
option(TEST7 "Enable Test 7" OFF)

# Set the compile definition
if(TEST1)
  add_definitions(-DTEST1)
elseif(TEST2)
  add_definitions(-DTEST2)
elseif(TEST3)
  add_definitions(-DTEST3)
elseif(TEST4)
  add_definitions(-DTEST4)
elseif(TEST5)
  add_definitions(-DTEST5)
elseif(TEST6)
  add_definitions(-DTEST6)
elseif(TEST7)
  add_definitions(-DTEST7)
endif()

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")

# Set the target source code
if(TEST1 OR TEST2 OR TEST3 OR TEST4 OR TEST5 OR TEST6 OR TEST7)
  set(sources src/main_test.cpp)
else()
  set(sources src/main.cpp)
endif()

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin") 

include_directories(/usr/local/include)
include_directories(/usr/local/opt/openssl/include)
link_directories(/usr/local/lib)
link_directories(/usr/local/opt/openssl/lib)
link_directories(/usr/local/Cellar/libuv/1.11.0/lib)

endif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin") 


add_executable(path_planning ${sources})

target_link_libraries(path_planning z ssl uv uWS)
