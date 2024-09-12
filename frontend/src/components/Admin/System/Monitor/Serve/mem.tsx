import { Card, Col, Descriptions, Progress, Row } from "antd";
import { getGB, getPercentValue } from "@/utils/utils";

export function Mem({ data }: any) {
  const { memInfo } = data;
  return (
    <>
      <Card title="内存">
        <Row>
          <Col span={6}>
            <Progress
              type="dashboard"
              percent={getPercentValue(
                (memInfo.total - memInfo.available) / memInfo.total
              )}
            />
          </Col>
          <Col span={18}>
            <Descriptions>
              <Descriptions.Item
                label="总空间"
                span={24}
                labelStyle={{ width: "50%" }}
              >
                {getGB(memInfo.total)} GB
              </Descriptions.Item>
              <Descriptions.Item
                label="已用空间"
                span={24}
                labelStyle={{ width: "50%" }}
              >
                {getGB(memInfo.total - memInfo.available)} GB
              </Descriptions.Item>
              <Descriptions.Item
                label="可用空间"
                span={24}
                labelStyle={{ width: "50%" }}
              >
                {getGB(memInfo.available)} GB
              </Descriptions.Item>
            </Descriptions>
          </Col>
        </Row>
      </Card>
    </>
  );
}
