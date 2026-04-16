import { Link } from "@tanstack/react-router";
import type { ReactNode } from "react";

export const HeaderLink = ({
  to,
  children,
  variant = "default",
  exact = false,
}: {
  to: string;
  children: ReactNode;
  variant?: "default" | "button";
  exact?: boolean;
}) => {
  const baseClassName =
    "inline-flex items-center rounded-md px-3 py-2 text-sm font-medium transition-colors duration-200";
  const defaultInactiveClassName = `${baseClassName} text-slate-600 hover:bg-slate-100 hover:text-slate-900`;
  const defaultActiveClassName = `${baseClassName} bg-slate-100 text-slate-900`;
  const buttonInactiveClassName = `${baseClassName} bg-slate-900 text-white hover:bg-slate-700`;
  const buttonActiveClassName = `${baseClassName} bg-slate-700 text-white`;

  const inactiveClassName = variant === "button" ? buttonInactiveClassName : defaultInactiveClassName;
  const activeClassName = variant === "button" ? buttonActiveClassName : defaultActiveClassName;

  return (
    <Link
      to={to}
      activeOptions={{
        exact,
      }}
      inactiveProps={{
        className: inactiveClassName,
      }}
      activeProps={{
        className: activeClassName,
      }}
    >
      {children}
    </Link>
  );
};
