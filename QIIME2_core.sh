#!/bin/bash
export PWD='/Users/kirstengrond/Desktop'
export CURDIR=${PWD}
export RESULTS=${SEQ}/results
export MPLCONFIGDIR=${CURDIR}/tmp
export TMPDIR=${CURDIR}/tmp
export NUMBA_CACHE_DIR=${TMPDIR}
export THREADS=3
export SEQ=${CURDIR}/sequences

### loop through qiime2 script for every directory.

for dir in ${SEQ}/* ; do
	cd $dir && sh /Users/kirstengrond/Desktop/Scripts/qiime2.sh ;
done
