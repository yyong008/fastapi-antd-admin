import { Link } from "@tanstack/react-router";
import type { ReactNode } from "react";

export const HeaderLink = ({
  to,
  children,
}: {
  to: string;
  children: ReactNode;
}) => {
  return (
    <Link
      to={to}
      inactiveProps={{
        className:
          "mr-[20px] hover:bg-yellow-300 px-[10px] py-[10px] rounded-[10px] hover:text-gray-900 hover:shadow-xl  border-gray-50",
      }}
      activeProps={{
        className:
          "mr-[20px] bg-yellow-300 px-[10px] py-[10px] rounded-[10px] hover:text-gray-900 hover:shadow-xl  border-gray-50",
      }}
    >
      {children}
    </Link>
  );
};
