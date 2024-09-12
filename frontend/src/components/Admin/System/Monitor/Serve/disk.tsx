import { Card, Col, Descriptions, Progress, Row } from "antd";
import { getGB, getPercentValue } from "@/utils/utils";

export function Disk({ data }: any) {
  const { diskInfo } = data;

  return (
    <>
      <Card title="磁盘">
        <Row>
          <Col span={6}>
            <Progress
              type="dashboard"
              percent={getPercentValue(
                (diskInfo.used) / diskInfo.size
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
                {getGB(diskInfo.size)} GB
              </Descriptions.Item>
              <Descriptions.Item
                label="已用空间"
                span={24}
                labelStyle={{ width: "50%" }}
              >
                {getGB(diskInfo.used)} GB
              </Descriptions.Item>
              <Descriptions.Item
                label="可用空间"
                span={24}
                labelStyle={{ width: "50%" }}
              >
                {getGB(diskInfo.available)} GB
              </Descriptions.Item>
            </Descriptions>
          </Col>
        </Row>
      </Card>
    </>
  );
}
