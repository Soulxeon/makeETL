import glob
import os
import pandas as pd
import settings
from visualCheck import visualcheck
from startCheck import filenamecheck

class EtlList:

    etl = pd.DataFrame(columns=['filePath', 'workspace', "dataset", "collection", "filename", 'imageryType',
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
            EtlList.etl.loc[len(EtlList.etl.index),'filePath'] = name
            EtlList.count += 1
            if EtlList.count % 1000 == 0:
                print("{} files processed succesfully".format(EtlList.count))
        
        EtlList.etl['dataset'] = EtlList.etl['filePath'].str.split("\\").str[self.n_dataset]
        EtlList.etl['collection'] = EtlList.etl['filePath'].str.split("\\").str[self.n_entity]
        EtlList.etl['filename'] = EtlList.etl['filePath'].str.split("\\").str[-1]
        EtlList.etl['status'] = 'Pending'
        EtlList.etl['flag_error'] = 'None'
        print("total of {} files processed succesfully".format(EtlList.count))    
    
    def readFolder(self):
        for name in glob.glob(self.path + '**\*.[jpt][pni][gf]*', recursive=True):
            dataset = name.split("\\")[self.n_dataset]
            entity = name.split("\\")[self.n_entity]
            filename = name.split("\\")[-1]
            imageType = filenamecheck.checkImageType(filename)
            if settings.depth_check is True:
                startdepth, enddepth = filenamecheck.checkStartEndDepth(filename)
            else:
                startdepth, enddepth = ['', '']

            if settings.img_process is True:
                exif_info, width, height, img_obs = visualcheck.infoPreview(name)
            else:
                exif_info, width, height, img_obs = ['', '', '', '']

            EtlList.etl.loc[len(EtlList.etl.index)] = [name,'',dataset, entity, filename, '', imageType, startdepth,
                                    enddepth,'','','Pending','None','', exif_info, width, height, img_obs]

            EtlList.count += 1
            if EtlList.count % 1000 == 0:
                print("{} files processed succesfully".format(EtlList.count))

        print("total of {} files processed succesfully".format(EtlList.count))

