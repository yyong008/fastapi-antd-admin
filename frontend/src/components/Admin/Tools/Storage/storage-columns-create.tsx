import { FormatTime } from "@/components/common/format-time";
import { ImageWithFallback } from "@/components/common/ImageWithFallback";

export const storageColumnsCreate = () => {
  return [
    {
      dataIndex: "path",
      title: "预览图",
      ellipsis: true,
      width: 80,
      render(_: string, record: any) {
        if (record?.type?.startsWith("image")) {
          return <ImageWithFallback style={{ width: "30px" }} src={record.path}  />
        }
        return record.path;
      },
    },
    {
      dataIndex: "name",
      title: "文件名",
      ellipsis: true,
    },
    {
      dataIndex: "ext_name",
      title: "文件后缀",
      ellipsis: true,
    },
    {
      dataIndex: "type",
      title: "类型",
      ellipsis: true,
    },
    {
      dataIndex: "size",
      title: "尺寸",
      ellipsis: true,
      render(_: string, record: any) {
        return <div>{(Number(record.size) / 1024).toFixed(0)}KB</div>;
      },
    },
    {
      dataIndex: "user_id",
      title: "上传者 id",
      ellipsis: true,
    },
    {
      dataIndex: "createdAt",
      title: "创建时间",
      ellipsis: true,
      renderText(text: string) {
        return <FormatTime timeStr={text} />;
      },
    },
  ];
};
