import { Outlet, createFileRoute } from "@tanstack/react-router";

import { Nav } from "@/components/Layout/Client/Nav";

export const Route = createFileRoute("/_client")({
  component: ClientNav,
});

function ClientNav() {
  return (
    <div className="flex justify-center relative bg-indigo-100 min-h-[100vh]">
      <Nav />
      <Outlet />
    </div>
  );
}
