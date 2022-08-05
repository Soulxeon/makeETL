import glob
import os
import pandas as pd
import settings
class EtlList:

    etl = pd.DataFrame(columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imageryType',
                                'imageType', 'startDepth', 'endDepth', 'startBox','endBox','status','flag_error',
                                'condition_error','exif', 'width', 'height','img_obs'])
    
    count = 0

    def __init__(self,dataset,entity):
        self.path = settings.path
        self.n_dataset = dataset
        self.n_entity = entity
        pass

    def emptyDirs(self):
        emptyDirs = list()
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            if len(dirnames) == 0 and len(filenames) == 0 :
                emptyDirs.append(dirpath)
        if len(emptyDirs) > 0:
            print("there are empty folders!")
            with open(self.path + 'Emptyfolder.txt', 'w') as f:
                for elem in emptyDirs: 
                    f.write(f'{elem}\n')              
            f.close()

    def readQuick(self):
        for name in glob.glob(self.path + '**\*.[jpt][pni][gf]*', recursive=True):
            EtlList.etl.loc[len(EtlList.etl.index),'filepath'] = name
            EtlList.count += 1
            if EtlList.count % 1000 == 0:
                print("{} files processed succesfully".format(EtlList.count))
        
        EtlList.etl['dataset'] = EtlList.etl['filepath'].str.split("\\").str[self.n_dataset]
        EtlList.etl['collection'] = EtlList.etl['filepath'].str.split("\\").str[self.n_entity]
        EtlList.etl['filename'] = EtlList.etl['filepath'].str.split("\\").str[-1]
        EtlList.etl['status'] = 'Pending'
        EtlList.etl['flag_error'] = 'None'
        print("total of {} files processed succesfully".format(EtlList.count))    

