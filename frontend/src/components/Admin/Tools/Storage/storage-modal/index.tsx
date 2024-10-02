import { Alert, Button, Progress, message } from "antd";
import { ModalForm, ProTable } from "@ant-design/pro-components";
import { STORAGE_MAX_FILES, STORAGE_MAX_SIZE, STORAGE_MAX_SIZE_MB } from "@/constants/upload";
import { useEffect, useRef, useState } from "react";

import { EditOutlined } from "@ant-design/icons";
import { uploadImages } from "./upload";

enum FileStatus {
  BeforeUpload,
  Uploading,
  Uploaded,
}

type StorageModalProps = {
  trigger?: React.ReactNode;
  refetch: any;
};

export function StorageModal(props: StorageModalProps) {
  const inputRef = useRef<HTMLInputElement>();
  const { trigger } = props;
  const [fileList, setFileList] = useState<any[]>([]);
  const chooseFileListRef = useRef<any[]>([]);

  const reset = () => {
    chooseFileListRef.current = [];
    setFileList([]);
  };
  useEffect(() => {
    return () => {
      reset();
    };
  }, []);

  return (
    <ModalForm
      title="文件上传"
      onFinish={async () => {
        await uploadImages({
          chooseFileListRef,
          fileList,
          setFileList,
          refetch: props.refetch,
        });
        return true;
      }}
      submitter={{
        searchConfig: {
          submitText: "开始上传",
        },
        submitButtonProps: {
          disabled: chooseFileListRef.current.length <= 0,
        },
      }}
      modalProps={{
        destroyOnClose: true,
        onCancel: () => {
          reset();
        },
      }}
      submitTimeout={2000}
      trigger={
        trigger ??
        ((
          <Button type={"primary"} icon={<EditOutlined />}>
            新建
          </Button>
        ) as any)
      }
    >
      <input
        ref={inputRef as any}
        type="file"
        multiple={true}
        style={{ display: "none" }}
        onChange={() => {
          const files = inputRef.current?.files ?? [];

          Array.from(files)?.forEach((file: any) => {
            if (file.size > STORAGE_MAX_SIZE) {
              return message.error(
                `单个文件不超过${STORAGE_MAX_SIZE_MB}MB，最多只能上传${STORAGE_MAX_FILES}个文件`
              );
            }
            chooseFileListRef.current?.push({
              file: file,
              url: URL.createObjectURL(file),
              name: file.name,
              size: file.size,
              type: file.type,
              status: FileStatus.BeforeUpload,
              progress: {
                loaded: 0,
                total: 0,
              },
              isError: false,
              isCompleted: false,
            });
          });
          setFileList(chooseFileListRef.current);
        }}
      />
      <Alert
        message={`单个文件不超过${STORAGE_MAX_SIZE_MB}MB，最多只能上传${STORAGE_MAX_FILES}个文件`}
        type="info"
        showIcon
      />
      <ProTable
        search={false}
        dataSource={fileList}
        columns={[
          {
            dataIndex: "url",
            title: "地址",
            ellipsis: true,
          },
          {
            dataIndex: "name",
            title: "文件名",
            width: 260,
            render(_, record) {
              const percent =
                (record.progress.loaded / record.progress.total) * 100;
              return (
                <div>
                  <div>{record.name}</div>
                  <Progress percent={percent}></Progress>
                </div>
              );
            },
          },
          {
            dataIndex: "size",
            title: "文件大小",
          },
          {
            dataIndex: "state",
            title: "状态",
          },
          {
            title: "操作",
            render(_, __, index) {
              return (
                <div
                  onClick={() => {
                    setFileList(fileList?.filter((_, i) => i !== index));
                  }}
                >
                  删除
                </div>
              );
            },
          },
        ]}
        toolBarRender={() => [
          <Button
            key="show"
            type="primary"
            onClick={() => {
              inputRef.current?.click();
            }}
          >
            选择文件
          </Button>,
        ]}
      />
    </ModalForm>
  );
}
