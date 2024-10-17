import { FormatTime } from "@/components/common/format-time";
import { Image } from "antd";
import { fallback_base_64_url } from "@/constants/fallback";

export const createFeedbackColumns = ({ refetch }: any) => [
  {
      dataIndex: "url",
      title: "反馈图片",
      render(_: any, record: any) {
        return (
          <div className="w-[40px]">
            <Image src={record.url} fallback={fallback_base_64_url}></Image>
          </div>
        );
      },
    },
    {
      dataIndex: "id",
      title: "反馈编号",
    },
    {
      dataIndex: "content",
      title: "反馈内容",
    },
    {
      dataIndex: "created_at",
      title: "反馈时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.created_at} />;
      },
    },
  ];
