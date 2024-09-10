import * as ic from "@ant-design/icons";

import { Dropdown, Form } from "antd";
import {
  removeLocalStorageRefreshToken,
  removeLocalStorageToken,
} from "@/utils/localstorage";

import React from "react";
import { useNavigate } from "@tanstack/react-router";

const { LogoutOutlined, UserOutlined } = ic;

type AvatarDropDownProps = {
  dom: any;
};

export const AvatarDropDown: React.FC<AvatarDropDownProps> = ({ dom }) => {
  const navigate = useNavigate();

  return (
    <Dropdown
      menu={{
        items: [
          {
            key: "profile-center",
            icon: <UserOutlined />,
            label: "personal-center",
            onClick: () => {
              navigate({ to: `/admin/profile/account` });
            },
          },
          {
            type: "divider",
          },
          {
            key: "logout",
            icon: (
              <Form method="post" action="/logout">
                <LogoutOutlined />
              </Form>
            ),
            label: "logout",
            onClick() {
              removeLocalStorageToken();
              removeLocalStorageRefreshToken();
              navigate({ to: `/admin/login` });
            },
          },
        ],
      }}
    >
      {dom}
    </Dropdown>
  );
};
