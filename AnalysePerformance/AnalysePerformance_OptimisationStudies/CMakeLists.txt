########################################################
# cmake file for building PandoraAnalysis
# @author Jan Engels, DESY
CMAKE_MINIMUM_REQUIRED(VERSION 2.8.2 FATAL_ERROR)
########################################################


# project name
PROJECT( PandoraAnalysis )


# project version
SET( PandoraAnalysis_VERSION_MAJOR 01 )
SET( PandoraAnalysis_VERSION_MINOR 00 )
SET( PandoraAnalysis_VERSION_PATCH 01 )


### CMAKE ###################################################################

FIND_PACKAGE( ILCUTIL COMPONENTS ILCSOFT_CMAKE_MODULES REQUIRED )

# load default settings from ILCSOFT_CMAKE_MODULES
INCLUDE( ilcsoft_default_settings )


### SOURCE ##################################################################

# include directories
INCLUDE_DIRECTORIES( BEFORE ./include ) # use BEFORE to fix problem on mac osx (case insensitive filesystem)

AUX_SOURCE_DIRECTORY( ./src PandoraAnalysis_SRCS )

# analysis executables
SET( PERFORMANCE_PROGRAMS AnalysePerformance )
SET( PROGRAMS ${PERFORMANCE_PROGRAMS} )

# require proper C++
ADD_DEFINITIONS( "-Wall -ansi -pedantic" )

# need long long for int64 for now
ADD_DEFINITIONS( "-Wno-long-long -Wno-sign-compare -fno-strict-aliasing" )


### DEPENDENCIES ############################################################

FIND_PACKAGE( Marlin 1.0 REQUIRED )
FIND_PACKAGE( MarlinUtil REQUIRED )
FIND_PACKAGE( LCIO REQUIRED )
FIND_PACKAGE( ROOT REQUIRED )

FOREACH( pkg Marlin MarlinUtil LCIO ROOT )
    IF( ${pkg}_FOUND )
        INCLUDE_DIRECTORIES( ${${pkg}_INCLUDE_DIRS} )
        LINK_LIBRARIES( ${${pkg}_LIBRARIES} )
        ADD_DEFINITIONS ( ${${pkg}_DEFINITIONS} )
    ENDIF()
ENDFOREACH()


### OUTPUT ##################################################################

# add library
ADD_SHARED_LIBRARY( PandoraAnalysis ${PandoraAnalysis_SRCS} )

FOREACH( program ${PERFORMANCE_PROGRAMS} )
    ADD_EXECUTABLE( ${program} ${PROJECT_SOURCE_DIR}/performance/${program}.cc )
ENDFOREACH( program )

FOREACH( program ${CALIBRATION_PROGRAMS} )
    ADD_EXECUTABLE( ${program} ${PROJECT_SOURCE_DIR}/calibration/${program}.cc )
ENDFOREACH( program )

FOREACH( program ${PROGRAMS} )
    TARGET_LINK_LIBRARIES( ${program} PandoraAnalysis )
ENDFOREACH( program )


### INSTALL #################################################################

# install library
INSTALL_SHARED_LIBRARY( PandoraAnalysis DESTINATION lib )

# install executables
FOREACH( program ${PROGRAMS} )
    INSTALL( TARGETS ${program} DESTINATION bin PERMISSIONS
        OWNER_READ OWNER_WRITE OWNER_EXECUTE
        GROUP_READ GROUP_EXECUTE
        WORLD_READ WORLD_EXECUTE )
ENDFOREACH( program )

# display some variables and write them to cache
DISPLAY_STD_VARIABLES()
