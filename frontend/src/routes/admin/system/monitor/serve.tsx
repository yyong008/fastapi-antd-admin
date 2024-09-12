import { Col, Row } from "antd";
import { useEffect, useState } from "react";

import { Cpu } from "@/components/Admin/System/Monitor/Serve/cpu";
import { Disk } from "@/components/Admin/System/Monitor/Serve/disk";
import { Mem } from "@/components/Admin/System/Monitor/Serve/mem";
import { OsRuntime } from "@/components/Admin/System/Monitor/Serve/os-runtime";
import { PageContainer } from "@ant-design/pro-components";
import { createFileRoute } from "@tanstack/react-router";
import { getMonitorServe } from "@/apis/admin/system/minitor.serve";

export const Route = createFileRoute("/admin/system/monitor/serve")({
  component: SystemMonitorServe,
});

function SystemMonitorServe() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState({
    nodeRuntime: {},
    osRuntime: {},
    pythonRuntime: {},
    diskInfo: {},
    memInfo: {},
    cupInfo: {},
    currentLoadInfo: {},
  });

  const getData = async () => {
    const res: any = await getMonitorServe();

    if (res && res?.code === 0) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, []);

  const {
    nodeRuntime,
    osRuntime,
    pythonRuntime,
    diskInfo,
    memInfo,
    cupInfo,
    currentLoadInfo,
  } = data;

  return (
    <PageContainer loading={loading}>
      <Row gutter={[16, 16]}>
        <Col span={12}>
          <OsRuntime data={{ nodeRuntime, osRuntime, pythonRuntime }} />
        </Col>
        <Col span={12}>
          <Disk data={{ diskInfo }} />
        </Col>
        <Col span={12}>
          <Cpu data={{ cupInfo, currentLoadInfo }} />
        </Col>
        <Col span={12}>
          <Mem data={{ memInfo }} />
        </Col>
      </Row>
    </PageContainer>
  );
}
