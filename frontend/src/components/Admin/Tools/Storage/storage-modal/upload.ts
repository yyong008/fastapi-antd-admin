import { ajax } from "rxjs/ajax";
import { combineLatest } from "rxjs";
import { message } from "antd";

export const uploadImages = async ({chooseFileListRef, fileList, setFileList , refetch }) => {
  const files = chooseFileListRef.current?.map((file) => file) ?? [];
  if (fileList.length <= 0) {
    message.error("请选择文件");
    return;
  } else if (fileList.length > 8) {
    message.error("最多只能上传8个文件");
    return;
  }
  const fileUpload$ = files.map((file) => {
    const formData = new FormData();
    formData.append("file", file.file);
    return ajax({
      method: "POST",
      url: `/api/admin/tools/storage/upload`,
      body: formData,
      includeUploadProgress: true,
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  });

  combineLatest(fileUpload$).subscribe({
    next(fileuploads: any) {
      // 所有的已经完成？
      const newFiles = fileuploads.map((uploadInfo, index) => {
        const info = {
          ...(chooseFileListRef?.current?.[index] ?? []),
          progress: {
            loaded: uploadInfo.originalEvent.loaded,
            total: uploadInfo.originalEvent.total,
          },
        };
        return info;
      });

      setFileList(() => {
        return newFiles;
      });
    },
    error(e) {
      console.log(e);
    },
    complete() {
      message.info("upload success");
      refetch?.();
    },
  });
};
