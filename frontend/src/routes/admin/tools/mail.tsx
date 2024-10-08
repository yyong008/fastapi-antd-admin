import "@/components/Admin/Tools/Mail/styles.css";

import { Button, Space } from "antd";
import { PageContainer, ProCard } from "@ant-design/pro-components";

import { Link } from "@tanstack/react-router";
import { MailForm } from "@/components/Admin/Tools/Mail/mail-form";
import { QuillEditor } from "@/components/common/quill-editor";
import { UnorderedListOutlined } from "@ant-design/icons"
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/admin/tools/mail")({
  component: ToolsMailRoute,
});

export function ToolsMailRoute() {
  const [content, setContent] = useState("");
  return (
    <PageContainer>
      <ProCard
        style={{ height: 600 }}
        title="发送邮件"
        tooltip="默认支持的邮箱服务包括：”QQ”、”163”、”126”、”iCloud”、”Hotmail”、”Yahoo”等"
        extra={
          <Space>
            <Link to={`/admin/tools/mail/list`}>
              <Button type="primary"><UnorderedListOutlined />查看所有模板</Button>
            </Link>
            <MailForm content={content} />
          </Space>
        }
      >
        <div style={{ height: "400px" }}>
          <QuillEditor content={content} setContent={setContent} />
        </div>
      </ProCard>
    </PageContainer>
  );
}
