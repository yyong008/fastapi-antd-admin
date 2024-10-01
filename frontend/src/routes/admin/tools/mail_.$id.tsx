import "@/components/Admin/Tools/MailDetail/styles.css";

import { Button, Space } from "antd";
import { Link, useParams } from "@tanstack/react-router";
import { PageContainer, ProCard } from "@ant-design/pro-components";
import { useEffect, useState } from "react";

import { MailForm } from "@/components/Admin/Tools/MailDetail/mail-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { UnorderedListOutlined } from "@ant-design/icons";
import { createFileRoute } from "@tanstack/react-router";
import { getMailById } from "@/apis/admin/tools/mail"

export const Route = createFileRoute("/admin/tools/mail/$id")({
  component: MailDetailRoute,
});

export function MailDetailRoute() {
  const [content, setContent] = useState("");
  const { id } = useParams({ strict: false });
  const [data, setData] = useState<any>();
  const [loading, setLoading] = useState(true);

  const getMailData = async () => {
    setLoading(true);
    const result: any = await getMailById(id);
    setLoading(false);
    if (result && result.code === 0) {
      setData(result.data);
    }
  }

  useEffect(() => {
    getMailData()
  }, [])

  useEffect(() => {

    setContent(data?.content);
  }, [data]);
  return (
    <PageContainer>
      <ProCard
        loading={loading}
        style={{ height: 600 }}
        title="修改邮件"
        tooltip="默认支持的邮箱服务包括：”QQ”、”163”、”126”、”iCloud”、”Hotmail”、”Yahoo”等"
        extra={
          <Space>
            <Link to={`/admin/tools/mail/list`}>
              <Button type="primary"><UnorderedListOutlined />查看所有模板</Button>
            </Link>
            <MailForm id={id} data={data} content={content} />
          </Space>
        }
      >
        <div style={{ height: "400px" }}>
          <QuillEditor
            initContent={data?.content}
            content={content}
            setContent={setContent}
          />
        </div>
      </ProCard>
    </PageContainer>
  );
}
