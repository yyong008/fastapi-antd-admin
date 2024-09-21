import { BlogContent } from "@/components/Client/BlogDetail/blog-content";
import { BlogHeader } from "@/components/Client/BlogDetail/blog-header";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogById } from "@/apis/client/blog";

export const Route = createFileRoute("/_client/blog/$id")({
  component: BlogDetailRoute,
  async loader({ params }) {
    const result: any = await getBlogById(Number(params.id));
    if (result && result.code === 0) {
      return result.data;
    }
  },
});

export function BlogDetailRoute() {
  const _data = Route.useLoaderData();
  const blog = _data;
  return (
    <div className="flex flex-col pt-[140px]  w-[70vw] min-h-[80vh] pb-[40px]">
      <div className="bg-white p-[20px] font-sans rounded-sm text-base/loose pb-[60px]">
        <BlogHeader blog={blog} />
        <BlogContent content={blog.content} />
      </div>
    </div>
  );
}
