#include "vanilla_defines/ww_defines.h"

void CreateHotestFunc(){
     cXyz scale = {1.0f, 1.0f, 1.0f};                                      // Initialize scale, position and angle
     cXyz position = {0.0f, 0.0f, 0.0f};;
     csXyz angle = {0.0f, 0.0f, 0.0f};
     int stagNo = g_dComIfG_gameInfo.mPlay.mStageData.parent.vtbl->getStagInfo; // This is the current stage number
     char* arcName = "Fa";
     //dRes_control_c resControl;
if (stagNo == 0){                                                          // Room transitions happens a bit differently on the sea stage (stageID 0)                                                      
                                                                           // Hence we work on a case by case basis, starting from sea
     short count;
     dRes_info_c* resPtr = dRes_control_c__getResInfo(arcName, g_dComIfG_gameInfo.mResCtrl.mObjectInfo, 0x24);
     if(resPtr != NULL){
      count = resPtr->mRefCount;
     }
     else{
      count = 0;
     }
     if(count < 1){                                                         // Create the hotest actor (0x00b5) only if no actor loads from Fa.arc
          fopAcM_create(0x00B5, 0, &position, dStage_roomControl_c__mStayNo, &angle, &scale, 0xFF, 0);
     }
}

else{                                                                       // If we are in any other stage than the sea, things are much simpler, since we ever only load one room at a time.
          fopAcM_create(0x00B5, 0, &position, dStage_roomControl_c__mStayNo, &angle, &scale, 0xFF, 0);
}
//dStage_stageDt_c dstage;
//dstage.parent.vtbl->getStagInfo;
//g_dComIfG_gameInfo.mPlay.mStageData.parent.vtbl->getStagInfo;
//g_dComIfG_gameInfo.mPlay.mpLinkActor->parent.parent.mCurrent.field3_0x13;
}
