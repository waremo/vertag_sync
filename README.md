# vertag_sync

A utility to sync github's tag and version string for source codes or scripts.


## Prerequisites/Installation

* version.py, vertag_sync.py are placed under the top directory of the
source code. (That is, should be placed at the same level with ".git")

* version.py is to contain version number, like `Version = "v2.0rc4"`
  (It is assumed to be imported by
  Python scripts.) 
  
* version.py should be added to tracking files.

* python-3.6 is required. 

  
## Invocation/Usage


### To check if version.py is valid

```
foo@bar:sourcetree1% python3 vertag_sync.py
```
 - if any modifications in tracked files, add "*" after Version in
		version.py
		
 - else: do nothing
	
### To synchronize version.py and the tag, 

do 

```
foo@bar:sourcetree1% python3 vertag_sync.py up
```

Then, the tool: 

  1. shows current Version in version.py and tag
  
  1. prompts the new version string
  
  1. write the new version into version.py
  
  1. commit all modified files
  
  1. put the new version into the tag 

## Notes

* To pull/push tags to/from remote, `--tag` option is required.

```
(pve36) fukuda@falcon:~/wrm_dms2% git push origin --tags
```

```
(pve36) fukuda@digoc02:~/wrm_dms2% git pull origin master --tags
From github.com:waremo/wrm_dms2
 * branch            master     -> FETCH_HEAD
 * [new tag]         v2.0rc1    -> v2.0rc1
 * [new tag]         v2.0rc2    -> v2.0rc2
 * [new tag]         v2.0rc3    -> v2.0rc3
 * [new tag]         v2.0rc4    -> v2.0rc4
 * [new tag]         v2.0rc5    -> v2.0rc5
Already up-to-date.
```
