import { FormatTime } from "@/components/common/format-time";
import { Image } from "antd";

export const createFeedbackColumns = ({ refetch }: any) => [
    {
      dataIndex: "id",
      title: "反馈编号",
    },
    {
      dataIndex: "content",
      title: "反馈内容",
    },
    {
      dataIndex: "url",
      title: "反馈图片",
      render(_: any, record: any) {
        return (
          <div className="w-[100px]">
            <Image src={record.url}></Image>
          </div>
        );
      },
    },
    {
      dataIndex: "created_at",
      title: "反馈时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.created_at} />;
      },
    },
  ];
