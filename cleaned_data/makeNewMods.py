#!/usr/bin/env python
# -utf-8- coding: utf-8 -utf-8-

#makeNewMods.py chd 150402
#makeStubs.py chd 150331

#revise per cmh2166
#original data downloaded from git yesterday

#current location:
#/home/cdeane/pubact/KEFAUVER/forpush/makeNewMods.py
#/home/cdeane/pubact/KEFAUVER/py/a2/makeNewMods.py


#purpose: revise most recent modsxml files per request.

#commandline: python makeNewMods.py source_dir target_dir
#             python makeNewMods.py mods15     new15 


#########KEFAUVER MODS ######################
#revision requests:
#
# 1. use current filenaming convention (do not change file names)
#
# 2.  directly after    <identifier type="local">KDP_1001</identifier>
#     add    
#             <identifier type="filename">KDP_1001.jp2</identifier>
#
# 3.  directly after    <digitalOrigin>reformattedDigital</digitalOrigin>
#     add    
#             <internetMediaType>image/jp2</internetMediaType>
#
# 4.  Inside the element <relatedItem type="host DisplayLabel="Project">
#     directly after </titleInfo>
#     add 
#             <location>
#		<url>http://digital.lib.utk.edu/collections/kefauvercollection</url>
#	      </location>
#
# 5.  directly under <recordOrigin>Created and edited in general conformance to MODS Guidelines (Version 3.5) </recordOrigin>
#     add
#		<recordChangeDate encoding="edtf">2015-04-02</recordChangeDate>
#
#########KEFAUVER MODS ######################


#########MAIN###############################
import os, sys
import datetime #for datetime
timestamp0=datetime.datetime.now()



pgm           = sys.argv[0] #name of pgm
if len(sys.argv)<2:
        print "usage: python "+pgm+" source_dir  target_dir"
        sys.exit(0)
        #
	#
source_dir    = sys.argv[1] #name of source dir   ###F,G(file in F)  
target_dir    = sys.argv[2] #name of target dir   ###H  

print pgm +" purpose: revise xml file per request\n" 

cmdline=">> python"

for item in sys.argv:
        s=item
        cmdline = cmdline +" "+item
        #
        #

if (os.path.isdir(source_dir) == False) :
        print "source_dir: no such dir: "+source_dir
        print "usage: "+cmdline
        sys.exit(0)
        #
        #

if (os.path.isdir(target_dir) == False) :
        print "target_dir: no such dir: "+target_dir
	cmdMakeTargetDir = "mkdir " + target_dir
	os.system(cmdMakeTargetDir)
	print target_dir + " has been created"
        #
        #


Flist = os.listdir(source_dir)
ct=0
for item in Flist:
	ct = ct+1
	s0 = item
	s1 = s0.replace("\n","")
	infile = source_dir+"/"+s1
	print "infile: " +infile
	G = open(infile,"r")
	Glist = G.readlines()
	G.close()
	Gall = ""
	Gdiscard = ""
	space3 = "   "
	space6="      "
	space12="            "
	stop= 0
	for item in Glist:
		t = item
		Gall = Gall +t
		if  stop==0 and t.find('identifier type="local">')>-1:
			t0 = t.lstrip(' ')
			t1 = t0.replace('<identifier type="local">','')
			t2 = t1.replace('<','.jp2<')
			t3 = t2.replace('  K','K',3)
			t4 = space3+'<identifier type="filename">'+t3
			Gall = Gall + t4
			stop = 1
			#
			#
		if  stop==1 and t.find('<digitalOrigin>')>-1:
			t0 = space6+'<internetMediaType>image/jp2</internetMediaType>'
			Gall = Gall + t0 +"\n"
			stop = 2
			#
			#
		if  stop==2 and t.find('<relatedItem type="host" displayLabel="Project">') >-1:
			stop = 3
			#
			#
		if stop == 3 and t.find('</titleInfo>')>-1:
			Gall = Gall +space6+ '<location>\n'
			Gall = Gall +space12+ '<url>http://digital.lib.utk.edu/collections/kefauvercollection</url>\n'
			Gall = Gall +space6+ '</location>\n'
			stop = 4
			#
			#
		if stop == 4 and t.find('<recordOrigin>Created')>-1:
			Gall = Gall +space6+ '<recordChangeDate encoding="edtf">2015-04-02</recordChangeDate>\n'
			stop = 5
			#
			#
		#
		#end for item in Glist:		
	outfile = target_dir+"/"+s1
	H = open(outfile,"w")
	H.write(Gall)
	H.close()
	#
	#


timestamp1=datetime.datetime.now()
duration=timestamp1-timestamp0
print "       begin time: "+str(timestamp0)
print "         end time: "+str(timestamp1)
print "         duration: "+str(duration)

print cmdline
sys.exit(0)

